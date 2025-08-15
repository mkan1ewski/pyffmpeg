from enum import Enum, auto
from itertools import count


class NodeType(Enum):
    INPUT = auto()
    FILTER = auto()
    OUTPUT = auto()


_id_generator = count()


def get_id():
    """Generates a new id."""
    return next(_id_generator)


class Node:
    def __init__(self, type: NodeType):
        self.id: str = get_id()
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

    def __init__(self, filename: str):
        super().__init__(NodeType.INPUT)
        self.filename: str = filename


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

    def __init__(self, source_node: Node, index: int = 0):
        self.source_node: Node = source_node
        self.index: int = index

    def _apply_filter(
        self, filter_name: str, params: dict, num_output_streams: int = 1
    ) -> list["Stream"]:
        """Creates a FilterNode and returns its output streams."""
        node = FilterNode(filter_name, params, [self], num_output_streams)
        return node.output_streams
