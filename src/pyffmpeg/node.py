from enum import Enum, auto


class NodeType(Enum):
    INPUT = auto()
    FILTER = auto()
    OUTPUT = auto()


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


class InputNode(ProcessableNode):
    """Nodes representing input files."""

    def __init__(self, filename: str):
        super().__init__(NodeType.INPUT)
        self.filename: str = filename

    def __eq__(self, other: "InputNode"):
        return self.filename == other.filename

    def __hash__(self):
        return hash(self.filename)


class OutputNode(Node):
    """Nodes representing output files."""

    def __init__(self, filename: str, inputs: list["Stream"]):
        super().__init__(NodeType.OUTPUT)
        self.inputs: list[Stream] = inputs
        self.filename: str = filename
        self.global_options: list[str] = []

    def get_output_mapping_args(self) -> list[str]:
        """Builds command args representing the output mapping from this output"""
        if len(self.inputs) == 1 and isinstance(self.inputs[0].source_node, InputNode):
            return [self.filename]
        args = []
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

    def get_args(self):
        sorter = GraphSorter(self)
        command_builder = CommandBuilder(sorter.sort())
        return command_builder.build_args()

    def overwrite_output(self) -> "OutputNode":
        """Adds global overwrite option"""
        self.global_options.append("-y")
        return self

    def __eq__(self, other: "OutputNode"):
        return (
            self.filename == other.filename
            and self.inputs == other.inputs
            and self.global_options == other.global_options
        )

    def __hash__(self):
        return hash((self.filename, tuple(self.inputs), tuple(self.global_options)))


class FilterNode(ProcessableNode):
    """Nodes representing filter operations."""

    def __init__(
        self,
        filter_name: str,
        postional_arguments: list,
        named_arguments: dict,
        inputs: list["Stream"],
        num_output_streams: int = 1,
    ):
        super().__init__(NodeType.FILTER, num_output_streams)
        self.filter_name: str = filter_name
        self.positional_arguments: list = postional_arguments
        self.named_arguments: dict = named_arguments
        self.inputs: list[Stream] = inputs

    def __eq__(self, other: "ProcessableNode"):
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
                tuple(self.positional_arguments),
                frozenset(self.named_arguments.items()),
                tuple(self.inputs),
            )
        )

    def get_command_string(self) -> str:
        """Builds a command string based on this filter"""
        input_streams = [f"[{input.index}]" for input in self.inputs]
        output_streams = [f"[{output.index}]" for output in self.output_streams]

        postional_arguments = [str(arg) for arg in self.positional_arguments]
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
        self.index: int = None

    def __eq__(self, other: "Stream"):
        return self.source_node == other.source_node

    def __hash__(self):
        return hash(self.source_node)

    def _apply_filter(
        self,
        filter_name: str,
        postional_arguments: list = [],
        named_arguments: dict = {},
        inputs: list["Stream"] = None,
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

    def scale(self, height: int, width: int) -> "Stream":
        """Scales to width and height."""
        return self._apply_filter(
            "scale", named_arguments={"height": height, "width": width}
        )[0]

    def split(self, num_outputs: int = 2) -> list["Stream"]:
        """Split into multiple identical streams."""
        return self._apply_filter(
            "split", postional_arguments=[num_outputs], num_output_streams=num_outputs
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
            named_arguments["x"] = x
        if y:
            named_arguments["y"] = y

        return self._apply_filter(
            "overlay",
            named_arguments=named_arguments,
            inputs=[self, overlay_stream],
        )[0]

    def trim(self, start_frame: int, end_frame: int):
        return self._apply_filter(
            "trim", named_arguments={"start_frame": start_frame, "end_frame": end_frame}
        )[0]

    def vflip(self):
        """Flip the input video vertically"""
        return self._apply_filter(filter_name="vflip")[0]

    def hflip(self):
        """Flip the input video horizontally"""
        return self._apply_filter(filter_name="hflip")[0]

    def crop(self, x: int, y: int, width: int, height: int):
        """Crop the input video to given dimensions"""
        return self._apply_filter("crop", postional_arguments=[width, height, x, y])[0]

    def concat(self, *streams: "Stream"):
        """Concatenate audio and video streams, joining them together one after the other"""
        return self._apply_filter(
            "concat",
            named_arguments={"n": len([self, *streams])},
            inputs=[self, *streams],
        )[0]

    def drawbox(
        self, x: int, y: int, width: int, height: int, color: str, thickness: int = None
    ):
        """Draw a colored box on the input image"""
        return self._apply_filter(
            "drawbox",
            postional_arguments=[x, y, width, height, color],
            named_arguments={"t": thickness},
        )[0]

    def output(self, *args) -> "OutputNode":
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

        return OutputNode(filename, streams)


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

        self.sorted.append(node)

    def label_streams(self):
        for node in self.sorted:
            if isinstance(node, InputNode):
                for stream in node.output_streams:
                    stream.index = f"{self.current_input_stream_index}"
                    self.current_input_stream_index += 1
            if isinstance(node, FilterNode):
                for stream in node.output_streams:
                    stream.index = f"s{self.current_filter_stream_index}"
                    self.current_filter_stream_index += 1


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
