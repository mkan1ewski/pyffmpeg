from enum import Enum, auto
from typing import Sequence


class NodeType(Enum):
    INPUT = auto()
    FILTER = auto()
    OUTPUT = auto()
    MERGED_OUTPUT = auto()


class Node:
    def __init__(self, type: NodeType):
        self.type: NodeType = type

    def get_args(self) -> list[str]:
        """Builds command arguments"""
        sorter = GraphSorter(self)
        command_builder = CommandBuilder(sorter.sort())
        return command_builder.build_args()


class ProcessableNode(Node):
    """Nodes that can be further processed with filters."""

    def __init__(self, type: NodeType, num_output_streams: int = 1):
        super().__init__(type)
        self.output_streams: list[Stream] = [
            Stream(self) for i in range(num_output_streams)
        ]


class InputNode(ProcessableNode):
    """Nodes representing input files."""

    def __init__(self, filename: str):
        super().__init__(NodeType.INPUT)
        self.filename: str = filename

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, InputNode):
            return NotImplemented
        return self.filename == other.filename

    def __hash__(self):
        return hash(self.filename)


class OutputNode(Node):
    """Nodes representing output files."""

    def __init__(
        self,
        filename: str,
        inputs: list["Stream"],
        output_options: dict[str, str | list[str]] = {},
    ):
        super().__init__(NodeType.OUTPUT)
        self.inputs: list[Stream] = inputs
        self.filename: str = filename
        self.output_options: dict[str, str | list[str]] = output_options
        self.global_options: list[str] = []

    def _normalize_output_options(self):
        """Replaces keys names in output_options from human readable (passed by the user)"""
        """to names existing in ffmpeg docs, prepares for later use to build command"""
        """Casts option values to string"""
        keys_names_mapping = {"video_bitrate": "b:v", "audio_bitrate": "b:a"}
        self.output_options = {
            keys_names_mapping.get(k, k): (
                [str(x) for x in v] if isinstance(v, (list, tuple)) else str(v)
            )
            for k, v in self.output_options.items()
        }

        if isinstance(self.output_options.get("video_size"), list):
            try:
                width, height = self.output_options["video_size"]
            except ValueError:
                raise ValueError(
                    "video_size must contain exactly two elements: (width, height)"
                )
            self.output_options["video_size"] = f"{width}x{height}"

    def get_output_mapping_args(self) -> list[str]:
        """Builds command args representing the output"""
        """Generates args for output options"""
        """Generates args for mapping streams to the output if neccessary"""
        args: list[str] = []
        self._normalize_output_options()

        for option_name, value in self.output_options.items():
            if isinstance(value, list):
                for single_value in value:
                    args.extend((f"-{option_name}", single_value))
            else:
                args.extend((f"-{option_name}", value))

        if len(self.inputs) == 1 and isinstance(self.inputs[0].source_node, InputNode):
            args.append(self.filename)
            return args

        for input in self.inputs:
            args.append("-map")
            args.append(
                f"[{input.index}]"
                if isinstance(input.source_node, FilterNode)
                else input.index
            )

        args.append(self.filename)

        return args

    def get_global_options(self) -> list[str]:
        """Returns global options"""
        return self.global_options

    def global_args(self, *args) -> "OutputNode":
        """Adds global options"""
        self.global_options.extend(args)
        return self

    def overwrite_output(self) -> "OutputNode":
        """Adds global overwrite option"""
        self.global_options.append("-y")
        return self

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, OutputNode):
            return NotImplemented
        return self.filename == other.filename and self.inputs == other.inputs

    def __hash__(self):
        return hash((self.filename, tuple(self.inputs), tuple(self.global_options)))


class MergedOutputNode(Node):
    """Node representing multiple outputs"""

    def __init__(self, outputs: Sequence[OutputNode]):
        super().__init__(NodeType.MERGED_OUTPUT)
        self.outputs: tuple = tuple(outputs)


class FilterNode(ProcessableNode):
    """Nodes representing filter operations."""

    def __init__(
        self,
        filter_name: str,
        postional_arguments: tuple,
        named_arguments: dict,
        inputs: list["Stream"],
        num_output_streams: int = 1,
    ):
        super().__init__(NodeType.FILTER, num_output_streams)
        self.filter_name: str = filter_name
        self.positional_arguments: tuple = postional_arguments
        self.named_arguments: dict = named_arguments
        self.inputs: list[Stream] = inputs

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FilterNode):
            return NotImplemented
        return (
            self.filter_name == other.filter_name
            and self.positional_arguments == other.positional_arguments
            and self.named_arguments == other.named_arguments
            and self.inputs == other.inputs
        )

    def __hash__(self):
        return hash(
            (
                self.filter_name,
                self.positional_arguments,
                frozenset(self.named_arguments.items()),
                tuple(self.inputs),
            )
        )

    def get_command_string(self) -> str:
        """Builds a command string based on this filter"""
        input_streams = [f"[{input.index}]" for input in self.inputs]
        output_streams = [f"[{output.index}]" for output in self.output_streams]

        postional_arguments = (str(arg) for arg in self.positional_arguments)
        named_arguments = [
            f"{name}={value}" for name, value in sorted(self.named_arguments.items())
        ]
        all_arguments = [*postional_arguments, *named_arguments]
        arguments_string = ":".join(all_arguments)

        return f"{''.join(input_streams)}{self.filter_name}{f'=' if arguments_string else ''}{arguments_string}{''.join(output_streams)}"


class Stream:
    """Represents a single output stream from a node."""

    def __init__(self, source_node: Node):
        self.source_node: Node = source_node
        self.index: str
        self.elemantary_streams: dict[str, TypedStream] = {}

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Stream):
            return NotImplemented
        return self.source_node == other.source_node

    def __hash__(self):
        return hash(self.source_node)

    @property
    def audio(self) -> "TypedStream":
        return self.elemantary_streams.setdefault("a", TypedStream("audio", self))

    @property
    def video(self) -> "TypedStream":
        return self.elemantary_streams.setdefault("v", TypedStream("video", self))

    def __getitem__(self, key: str) -> "TypedStream":
        """Allows accessing elementary stream contained in this Stream"""
        mapping = {"a": "audio", "v": "video"}
        if not isinstance(key, str) or len(key) != 1:
            raise TypeError("Expected string index (e.g. 'a')")

        if key not in mapping:
            raise KeyError(f"Invalid stream type: {key!r}. Expected 'a' or 'v'.")
        return self.elemantary_streams.setdefault(key, TypedStream(mapping[key], self))

    @property
    def node(self):
        """Returns the list of output streams produced by the filter node
        that generated this stream."""
        if not isinstance(self.source_node, FilterNode):
            raise AttributeError(".node is only available on filter outputs")
        return self.source_node.output_streams

    def _apply_filter(
        self,
        filter_name: str,
        postional_arguments: tuple = (),
        named_arguments: dict[str, str] = {},
        inputs: list["Stream"] | None = None,
        num_output_streams: int = 1,
    ) -> list["Stream"]:
        """Creates a FilterNode and returns its output streams."""
        node = FilterNode(
            filter_name,
            postional_arguments,
            named_arguments,
            inputs or [self],
            num_output_streams,
        )
        return node.output_streams

    def filter(self, filter_name: str, *args, **kwargs) -> "Stream":
        """Custom filter with a single input and a single output"""
        return self._apply_filter(filter_name, args, kwargs)[0]

    def scale(self, height: int, width: int) -> "Stream":
        """Scales to width and height."""
        return self._apply_filter(
            "scale", named_arguments={"height": str(height), "width": str(width)}
        )[0]

    def split(self, num_outputs: int = 2) -> list["Stream"]:
        """Split into multiple identical streams."""
        return self._apply_filter(
            "split", postional_arguments=(num_outputs,), num_output_streams=num_outputs
        )

    def asplit(self, num_outputs: int = 2) -> list["Stream"]:
        """Split into multiple identical audio streams."""
        return self._apply_filter(
            "asplit", postional_arguments=(num_outputs,), num_output_streams=num_outputs
        )

    def overlay(
        self,
        overlay_stream: "Stream",
        x: int | None = None,
        y: int | None = None,
        eof_action: str = "repeat",
    ) -> "Stream":
        """Overlay another video stream on top of this one."""
        named_arguments = {"eof_action": eof_action}
        if x:
            named_arguments["x"] = str(x)
        if y:
            named_arguments["y"] = str(y)

        return self._apply_filter(
            "overlay",
            named_arguments=named_arguments,
            inputs=[self, overlay_stream],
        )[0]

    def trim(self, start_frame: int, end_frame: int):
        return self._apply_filter(
            "trim",
            named_arguments={
                "start_frame": str(start_frame),
                "end_frame": str(end_frame),
            },
        )[0]

    def vflip(self):
        """Flip the input video vertically"""
        return self._apply_filter(filter_name="vflip")[0]

    def hflip(self):
        """Flip the input video horizontally"""
        return self._apply_filter(filter_name="hflip")[0]

    def crop(self, x: int, y: int, width: int, height: int):
        """Crop the input video to given dimensions"""
        return self._apply_filter("crop", postional_arguments=(width, height, x, y))[0]

    def concat(self, *streams: "Stream", **kwargs):
        """Concatenate audio and video streams, joining them together one after the other"""
        video_stream_count = kwargs.get("v", 1)
        audio_stream_count = kwargs.get("a", 0)
        output_stream_count = video_stream_count + audio_stream_count
        input_stream_count = int(len([self, *streams]))
        if (input_stream_count % output_stream_count) != 0:
            raise ValueError(
                f"Expected concat input streams to have length multiple of {output_stream_count} (v={video_stream_count}, a={audio_stream_count}); got {input_stream_count}"
            )
        kwargs["n"] = int(input_stream_count / output_stream_count)
        return self._apply_filter(
            "concat",
            named_arguments=kwargs,
            inputs=[self, *streams],
            num_output_streams=output_stream_count,
        )[0]

    def drawbox(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: str,
        thickness: int | None = None,
    ):
        """Draw a colored box on the input image"""
        return self._apply_filter(
            "drawbox",
            postional_arguments=(x, y, width, height, color),
            named_arguments={"t": str(thickness)},
        )[0]

    def output(self, *args, **kwargs) -> "OutputNode":
        streams = []
        filename = None

        streams.append(self)

        for arg in args:
            if isinstance(arg, Stream):
                streams.append(arg)
            elif isinstance(arg, str):
                filename = arg
            else:
                raise TypeError(f"Unexpected argument type: {type(arg)}")

        if not filename:
            raise ValueError("No output filename provided to output()")

        return OutputNode(filename, streams, output_options=kwargs)


class TypedStream(Stream):
    """Elementary stream representing specific type of media out of those contained within a Stream"""

    def __init__(self, type: str, source_stream: Stream):
        self.type = type
        self.source_node = source_stream.source_node
        self.index: str

    def __getitem__(self, _):
        """Raises ValueError"""
        mapping = {"audio": "a", "video": "v"}
        raise ValueError(f"Stream already has a selector: {mapping[self.type]}")


class GraphSorter:
    def __init__(self, output: Node):
        self.start_node: Node = output
        self.visited: set[Node] = set()
        self.sorted: list[Node] = []
        self.current_input_stream_index = 0
        self.current_filter_stream_index = 0

    def sort(self) -> list[Node]:
        self._sort(self.start_node)
        type_order = {InputNode: 0, FilterNode: 1, OutputNode: 2}
        self.sorted.sort(key=lambda x: type_order[type(x)])
        self.label_streams()
        return self.sorted

    def _sort(self, node: Node):
        if node in self.visited:
            return
        self.visited.add(node)

        if node.type in [NodeType.FILTER, NodeType.OUTPUT]:
            for stream in node.inputs:
                self._sort(stream.source_node)

        if node.type == NodeType.MERGED_OUTPUT:
            for output in node.outputs:
                self._sort(output)
            return

        self.sorted.append(node)

    def label_streams(self):
        for node in self.sorted:
            if isinstance(node, InputNode):
                for stream in node.output_streams:
                    stream.index = str(self.current_input_stream_index)
                    self.label_elementary_streams(stream)
                    self.current_input_stream_index += 1
            if isinstance(node, FilterNode):
                for stream in node.output_streams:
                    stream.index = f"s{self.current_filter_stream_index}"
                    self.label_elementary_streams(stream)
                    self.current_filter_stream_index += 1

    def label_elementary_streams(self, stream: Stream):
        for type, elementary_stream in stream.elemantary_streams.items():
            elementary_stream.index = f"{stream.index}:{type}"


class CommandBuilder:
    def __init__(self, nodes: list[Node]):
        self.nodes = nodes

    def build_args(self):
        args = []
        filters = []
        outputs = []
        global_options = []
        filter_complex = False
        for node in self.nodes:
            if isinstance(node, InputNode):
                args.extend(["-i", node.filename])
            if isinstance(node, FilterNode):
                if not filter_complex:
                    args.append("-filter_complex")
                    filter_complex = True

                filters.append(node.get_command_string())
            if isinstance(node, OutputNode):
                outputs.extend(node.get_output_mapping_args())
                global_options.extend(node.get_global_options())

        if filters:
            args.append(";".join(filters))
        args.extend([*outputs, *global_options])

        return args
