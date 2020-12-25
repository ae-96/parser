from node import Node


class Tree:
    def __init__(self):
        # this is a virtual root which has no name and no shape, root has only listofchild
        # the first child must be attached to nothing
        # all other children must be attached to each other
        self.root = Node()
