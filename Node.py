class node :
    def __init__(self):
        # this node is attached to all listofseparatedchild and ONLY the first element in listofattachedchild
        # from the second elemnt in listofattachedchild : each element is attached to the pervious element
        self.name=''
        self.shape=''
        self.listofseparatedchild=[]
        self.listofattachedchild = []