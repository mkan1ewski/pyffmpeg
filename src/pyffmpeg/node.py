from enum import Enum, auto


class NodeType(Enum):
    INPUT = auto()
    FILTER = auto()
    OUTPUT = auto()


class Node:
    def __init__(self, id: str, type: NodeType):
        self.id: str = id
        self.type: NodeType = type
