from pyffmpeg._utils import (
    escape_filter_option,
    escape_filter_description,
    escape_text_content,
)
from pyffmpeg.errors import Error
from enum import Enum, auto
from typing import Sequence
import subprocess


class NodeType(Enum):
    INPUT = auto()
    FILTER = auto()
    OUTPUT = auto()
    MERGED_OUTPUT = auto()


class Node:
    def __init__(self, type: NodeType):
        self.type: NodeType = type


class ProcessableNode(Node):
    """Nodes that can be further processed with filters."""

    def __init__(self, type: NodeType, num_output_streams: int = 1):
        super().__init__(type)
        self.output_streams: list[Stream] = [
            Stream(self) for i in range(num_output_streams)
        ]


class RunnableNode(Node):
    def __init__(self, type):
        super().__init__(type)
        self.global_options: list[str] = []

    def global_args(self, *args) -> "RunnableNode":
        """Adds global options"""
        self.global_options.extend(args)
        return self

    def overwrite_output(self) -> "RunnableNode":
        """Adds global overwrite option"""
        self.global_options.append("-y")
        return self

    def _compile_global_kwargs(self, options_dict: dict) -> list[str]:
        """Converts kwargs to list"""
        args = []
        key_map = {
            "overwrite_output": "y",
            "log_level": "loglevel",
            "quiet": "loglevel",
        }
        for key, value in options_dict.items():
            if key == "quiet" and value is True:
                args.extend(["-loglevel", "quiet"])
                continue

            flag_name = key_map.get(key, key)

            if value is True:
                # -y with overwrite_output=True
                args.append(f"-{flag_name}")
            elif value is not None and value is not False:
                # handles for example log_level="error"
                args.extend([f"-{flag_name}", str(value)])
        return args

    def get_args(self, overwrite_output=False, **global_options) -> list[str]:
        """Builds command arguments"""
        global_options["overwrite_output"] = overwrite_output
        kwargs_args = self._compile_global_kwargs(global_options)
        sorter = GraphSorter(self)
        command_builder = CommandBuilder(
            sorter.sort(), self.global_options + kwargs_args
        )
        return command_builder.build_args()

    def compile(
        self, cmd: str = "ffmpeg", overwrite_output: bool = False, **global_options
    ) -> list[str]:
        """Builds command line arguments for invoking ffmpeg"""
        if isinstance(cmd, str):
            cmd = [cmd]
        elif not isinstance(cmd, list):
            cmd = list(cmd)
        return cmd + self.get_args(overwrite_output=overwrite_output, **global_options)

    def run(
        self,
        cmd: str | list[str] = "ffmpeg",
        capture_stdout: bool = False,
        capture_stderr: bool = False,
        input: bytes | None = None,
        quiet: bool = False,
        overwrite_output: bool = False,
        cwd: str | None = None,
        compile_function=None,
    ) -> tuple[bytes | None, bytes | None]:
        """Execute the ffmpeg command represented by a RunnableNode"""
        if not isinstance(self, RunnableNode):
            raise TypeError(f"Expected RunnableNode, got {type(self)}")

        compile_function = compile_function or self.compile
        cmdline = compile_function(
            self,
            cmd=cmd,
            overwrite_output=overwrite_output,
            quiet=quiet,
        )

        stdout = subprocess.PIPE if capture_stdout else None
        stderr = subprocess.PIPE if capture_stderr else None

        try:
            process = subprocess.run(
                cmdline,
                input=input,
                stdout=stdout,
                stderr=stderr,
                cwd=cwd,
                check=True,
            )
            return process.stdout, process.stderr
        except subprocess.CalledProcessError as e:
            raise Error(
                "ffmpeg error (see stderr output for detail)",
                stdout=e.stdout,
                stderr=e.stderr,
            )


class InputNode(ProcessableNode):
    """Nodes representing input files."""

    def __init__(self, filename: str, options: dict[str, str] = None):
        super().__init__(NodeType.INPUT)
        self.filename: str = filename
        self.options: dict[str, str] = options

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, InputNode):
            return NotImplemented
        return self.filename == other.filename

    def __hash__(self) -> int:
        return hash(self.filename)

    def get_input_args(self) -> list[str]:
        """Returns command args for this input"""
        args = []
        for option_name, value in self.options.items():
            args.extend([f"-{option_name}", str(value)])
        args.extend(["-i", self.filename])
        return args


class OutputNode(RunnableNode):
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

    def get_output_args(self, enforce_output_mapping) -> list[str]:
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

        if (
            len(self.inputs) == 1
            and isinstance(self.inputs[0].source_node, InputNode)
            and not enforce_output_mapping
        ):
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

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, OutputNode):
            return NotImplemented
        return self.filename == other.filename and self.inputs == other.inputs

    def __hash__(self) -> int:
        return hash((self.filename, tuple(self.inputs)))


class MergedOutputNode(RunnableNode):
    """Node representing multiple outputs"""

    def __init__(self, outputs: Sequence[OutputNode]):
        super().__init__(NodeType.MERGED_OUTPUT)
        self.outputs: tuple[OutputNode] = tuple(outputs)


class FilterNode(ProcessableNode):
    """Nodes representing filter operations."""

    def __init__(
        self,
        filter_name: str,
        postional_arguments: tuple[str],
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

    def __hash__(self) -> int:
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
            f"{name}={escape_filter_description(escape_filter_option(value))}"
            for name, value in sorted(self.named_arguments.items())
        ]
        all_arguments = [*postional_arguments, *named_arguments]
        arguments_string = ":".join(all_arguments)

        return f"{''.join(input_streams)}{self.filter_name}{f'=' if arguments_string else ''}{arguments_string}{''.join(output_streams)}"


class Stream:
    """Represents a single output stream from a node."""

    def __init__(self, source_node: Node):
        self.source_node: Node = source_node
        self.index: str
        self.elemantary_streams: dict[str, TypedStream | IndexedStream] = {}

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Stream):
            return NotImplemented
        return self.source_node == other.source_node

    def __hash__(self) -> int:
        return hash(self.source_node)

    @property
    def audio(self) -> "TypedStream":
        return self.elemantary_streams.setdefault("a", TypedStream("audio", self))

    @property
    def video(self) -> "TypedStream":
        return self.elemantary_streams.setdefault("v", TypedStream("video", self))

    def __getitem__(self, key: str) -> "TypedStream | IndexedStream":
        """Allows accessing elementary stream contained in this Stream"""
        mapping = {"a": "audio", "v": "video"}
        if not isinstance(key, str) or len(key) != 1:
            raise TypeError("Expected string index (e.g. 'a')")

        if key in mapping:
            stream_type = mapping[key]
            return self.elemantary_streams.setdefault(
                key, TypedStream(stream_type, self)
            )

        if key.isdigit():
            return self.elemantary_streams.setdefault(key, IndexedStream(self))

        raise KeyError(
            f"Invalid stream key: {key!r}. Expected 'a', 'v', or a numeric index like '1'."
        )

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

    def filter(
        self, filter_name: str, inputs: list["Stream"] = [], **kwargs
    ) -> "Stream":
        """Custom filter with single or many inputs and a single output"""
        return self._apply_filter(
            filter_name, named_arguments=kwargs, inputs=[self, *inputs]
        )[0]

    def filter_multi_output(
        self, filter_name: str, inputs: list["Stream"] = [], **kwargs
    ) -> "FilterMultiOutput":
        """Creates a custom filter allowing dynamic creation of output streams"""
        node = FilterNode(
            filter_name=filter_name,
            named_arguments=kwargs,
            inputs=[self, *inputs],
            num_output_streams=0,
        )
        return FilterMultiOutput(node)

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

    def trim(self, **kwargs) -> "Stream":
        return self._apply_filter("trim", named_arguments=kwargs)[0]

    def vflip(self) -> "Stream":
        """Flip the input video vertically"""
        return self._apply_filter(filter_name="vflip")[0]

    def hflip(self) -> "Stream":
        """Flip the input video horizontally"""
        return self._apply_filter(filter_name="hflip")[0]

    def crop(self, x: int, y: int, width: int, height: int) -> "Stream":
        """Crop the input video to given dimensions"""
        return self._apply_filter("crop", postional_arguments=(width, height, x, y))[0]

    def concat(self, *streams: "Stream", **kwargs) -> "Stream":
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
    ) -> "Stream":
        """Draw a colored box on the input image"""
        return self._apply_filter(
            "drawbox",
            postional_arguments=(x, y, width, height, color),
            named_arguments={"t": str(thickness)},
        )[0]

    def drawtext(self, text: str, **kwargs) -> "Stream":
        kwargs["text"] = escape_text_content(text)
        return self._apply_filter("drawtext", named_arguments=kwargs)[0]

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


class IndexedStream(Stream):
    """Elementary stream represented by index within the containing stream"""

    def __init__(self, source_stream: Stream):
        self.source_node = source_stream.source_node
        self.label: str

    def __getitem__(self, _):
        """Raises ValueError"""
        raise ValueError(f"Stream already has a selector")


class GraphSorter:
    def __init__(self, output: RunnableNode):
        self.start_node: RunnableNode = output
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

    def _sort(self, node: Node) -> None:
        if node in self.visited:
            return
        self.visited.add(node)

        if isinstance(node, (FilterNode, OutputNode)):
            for stream in node.inputs:
                self._sort(stream.source_node)

        if isinstance(node, MergedOutputNode):
            for output in node.outputs:
                self._sort(output)
            return

        self.sorted.append(node)

    def label_streams(self) -> None:
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
    def __init__(self, nodes: list[Node], global_options: list = []):
        self.nodes: list[Node] = nodes
        self.global_options: list[str] = global_options

    def build_args(self) -> list[str]:
        args: list[str] = []
        filters = []
        outputs = []
        filter_complex: bool = False
        multi_input: bool = True if isinstance(self.nodes[1], InputNode) else False
        enforce_output_mapping: bool = False
        for node in self.nodes:
            if isinstance(node, InputNode):
                args.extend(node.get_input_args())
            if isinstance(node, FilterNode):
                if not filter_complex:
                    args.append("-filter_complex")
                    filter_complex = True

                filters.append(node.get_command_string())
            if isinstance(node, OutputNode):
                outputs.extend(node.get_output_args(enforce_output_mapping))
                if multi_input:
                    enforce_output_mapping = True

        if filters:
            args.append(";".join(filters))
        args.extend([*outputs])

        args.extend(self.global_options)

        return args


class FilterMultiOutput:
    """Filter node wrapper which allows creating arbitrary outputs for the filter node dynamically"""

    def __init__(self, filter_node: FilterNode):
        self.filter_node = filter_node
        self.stream_cache: dict[str, Stream] = {}

    def __getitem__(self, key: str | int) -> "Stream":
        """Returns new or existing stream under label"""
        label = str(key)
        if label in self.stream_cache:
            return self.stream_cache[label]

        new_stream = Stream(self.filter_node)
        self.filter_node.output_streams.append(new_stream)
        self.stream_cache[label] = new_stream
        return new_stream
