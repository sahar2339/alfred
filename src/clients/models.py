from enum import Enum

class ObjectKinds(str, Enum):
    POD = "Pod"
    NODE = "Node"
    