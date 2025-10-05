from enum import Enum, auto
from itertools import count


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
            Stream(self, i) for i in range(num_output_streams)
        ]


class InputNode(ProcessableNode):
    """Nodes representing input files."""

    _id_generator = count()

    def __init__(self, filename: str):
        super().__init__(NodeType.INPUT)
        self.filename: str = filename
        self.input_index = next(InputNode._id_generator)


class OutputNode(Node):
    """Nodes representing output files."""

    def __init__(self, filename: str, inputs: list["Stream"]):
        super().__init__(NodeType.OUTPUT)
        self.inputs: list[Stream] = inputs
        self.filename: str = filename


class FilterNode(ProcessableNode):
    """Nodes representing filter operations."""

    _label_generator = count()

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
        self.label = f"f{next(FilterNode._label_generator)}"


class Stream:
    """Represents a single output stream from a node."""

    def __init__(self, source_node: Node, index: int = 0):
        self.source_node: Node = source_node
        self.index: int = index

    def get_command_repr(self) -> str:
        return (
            f"[{self.source_node.input_index}]"
            if self.source_node.type == NodeType.INPUT
            else f"[{self.source_node.label}_{self.index}]"
        )

    def _apply_filter(
        self,
        filter_name: str,
        params: dict,
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

    def output(self, filename: str, inputs: list["Stream"] = None):
        inputs = inputs + [self] if inputs else [self]
        output = OutputNode(filename, inputs)
        sorter = GraphSorter(output)
        return sorter.sort()


class GraphSorter:
    def __init__(self, output: Node):
        self.start_node: Node = output
        self.visited: set[Node] = set()
        self.sorted: list[Node] = []

    def sort(self) -> list[Node]:
        self._sort(self.start_node)
        return self.sorted

    def _sort(self, node: Node):
        if node in self.visited:
            return
        self.visited.add(node)

        if node.type in [NodeType.FILTER, NodeType.OUTPUT]:
            for stream in node.inputs:
                self._sort(stream.source_node)

        self.sorted.append(node)


class CommandBuilder:
    def __init__(self, nodes: list[Node]):
        self.nodes = nodes

    def build_command(self):
        inputs = []
        filters = []
        for node in self.nodes:
            if node.type == NodeType.INPUT:
                inputs.extend(["-i", node.filename])
            if node.type == NodeType.FILTER:
                input_streams = []
                for stream in node.inputs:
                    # input_streams.append(f"[{stream.source_node.label}_{stream.index}]")
                    input_streams.append(stream.get_command_repr())
                output_streams = [
                    f"[{node.label}_{i}]" for i in range(len(node.output_streams))
                ]
                filters.append(
                    "".join(input_streams)
                    + f" {node.filter_name} "
                    + "".join(output_streams)
                )
        command = (
            "ffmpeg "
            + " ".join(inputs)
            + ' -filter_complex " '
            + " ; ".join(filters)
            + ' "'
        )
        return command
