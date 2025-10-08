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


class OutputNode(Node):
    """Nodes representing output files."""

    def __init__(self, filename: str, inputs: list["Stream"]):
        super().__init__(NodeType.OUTPUT)
        self.inputs: list[Stream] = inputs
        self.filename: str = filename

    def get_args(self):
        sorter = GraphSorter(self)
        command_builder = CommandBuilder(sorter.sort())
        return command_builder.build_args()

    def overwrite_output(self):
        return self


class FilterNode(ProcessableNode):
    """Nodes representing filter operations."""

    def __init__(
        self,
        filter_name: str,
        params: dict,
        inputs: list["Stream"],
        num_output_streams: int = 1,
    ):
        super().__init__(NodeType.FILTER, num_output_streams)
        self.filter_name: str = filter_name
        self.params: dict = params
        self.inputs: list[Stream] = inputs


class Stream:
    """Represents a single output stream from a node."""

    def __init__(self, source_node: Node):
        self.source_node: Node = source_node
        self.index: int = None

    def _apply_filter(
        self,
        filter_name: str,
        params: dict = {},
        inputs: list["Stream"] = None,
        num_output_streams: int = 1,
    ) -> list["Stream"]:
        """Creates a FilterNode and returns its output streams."""
        node = FilterNode(filter_name, params, inputs or [self], num_output_streams)
        return node.output_streams

    def scale(self, height: int, width: int) -> "Stream":
        """Scales to width and height."""
        return self._apply_filter("scale", {"height": height, "width": width})[0]

    def split(self, num_outputs: int = 2) -> list["Stream"]:
        """Split into multiple identical streams."""
        return self._apply_filter("split", {}, num_output_streams=num_outputs)

    def overlay(self, overlay_stream: "Stream", x: int = 0, y: int = 0) -> "Stream":
        """Overlay another video stream on top of this one."""
        return self._apply_filter(
            "overlay", {"x": x, "y": y}, inputs=[self, overlay_stream]
        )[0]

    def trim(self, start_frame: int, end_frame: int):
        return self._apply_filter(
            "trim", {"start_frame": start_frame, "end_frame": end_frame}
        )[0]

    def vflip(self):
        """Flip the input video vertically"""
        return self._apply_filter(filter_name="vflip")[0]

    def hflip(self):
        """Flip the input video horizontally"""
        return self._apply_filter(filter_name="hflip")[0]

    def crop(self, x: int, y: int, width: int, height: int):
        """Crop the input video to given dimensions"""
        return self._apply_filter(
            "crop", {"x": x, "y": y, "width": width, "height": height}
        )[0]

    def concat(self, *streams: "Stream"):
        """Concatenate audio and video streams, joining them together one after the other"""
        return self._apply_filter("concat", {}, [self, *streams])[0]

    def drawbox(
        self, x: int, y: int, width: int, height: int, color: str, thickness: int = None
    ):
        """Draw a colored box on the input image"""
        return self._apply_filter(
            "drawbox",
            {"x": x, "y": y, "width": width, "height": height, "thickness": thickness},
        )[0]

    def output(self, filename: str, inputs: list["Stream"] = None) -> OutputNode:
        inputs = inputs + [self] if inputs else [self]
        output = OutputNode(filename, inputs)
        return output


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
        return self.sorted

    def _sort(self, node: Node):
        if node in self.visited:
            return
        self.visited.add(node)

        if node.type in [NodeType.FILTER, NodeType.OUTPUT]:
            for stream in node.inputs:
                self._sort(stream.source_node)

            for stream in node.inputs:
                if isinstance(stream.source_node, FilterNode):
                    stream.index2 = f"s{self.current_filter_stream_index}"
                    self.current_filter_stream_index += 1
                if isinstance(stream.source_node, InputNode):
                    stream.index2 = f"{self.current_input_stream_index}"
                    self.current_input_stream_index += 1

        self.sorted.append(node)


class CommandBuilder:
    def __init__(self, nodes: list[Node]):
        self.nodes = nodes

    def build_args(self):
        args = []
        for node in self.nodes:
            if isinstance(node, InputNode):
                args.extend(["-i", node.filename])
            if isinstance(node, FilterNode):
                input_streams = [f"[{input.index2}]" for input in node.inputs]
                args.append(
                    f"{''.join(input_streams)}{node.filter_name}{''.join([f'[{stream.index2}]' for stream in node.output_streams])};"
                )
            if isinstance(node, OutputNode):
                args.append(node.filename)

        return args
