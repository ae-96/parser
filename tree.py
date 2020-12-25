from node import Node


class Tree:
    def __init__(self):
        # this is a virtual root which has no name,no shape and no separated children, root has only listofattachedchild
        self.root = Node()
