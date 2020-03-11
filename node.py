import struture_exception


class Node:

    def __init__(self, info=None, next_=None):
        self.__info = info
        self.__next = self.setNext(next_)

    def getInfo(self):
        return self.__info

    def setInfo(self, value):
        self.__info = value

    def getNext(self):
        return self.__next

    def setNext(self, node):
        if isinstance(node, Node) or node is None:
            self.__next = node
        else:
            raise struture_exception.NodeTypeError(node)

    def __str__(self):
        return "(%s)" % str(self.__info)
