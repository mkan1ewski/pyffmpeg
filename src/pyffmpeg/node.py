from enum import Enum, auto


class NodeType(Enum):
    INPUT = auto()
    FILTER = auto()
    OUTPUT = auto()


class Node:
    def __init__(self, id: str, type: NodeType):
        self.id: str = id
        self.type: NodeType = type


class ProcessableNode(Node):
    """Nodes that can be further processed with filters."""


class InputNode(ProcessableNode):
    """Nodes representing input files."""

    def __init__(self, id, filename):
        super().__init__(id, NodeType.INPUT)
        self.filename: str = filename
