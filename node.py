import struture_exception


class Node:

    def __init__(self, data: any = None, next_=None):
        self.__data: any = data
        self.__next: Node = self.setNext(next_)

    def getData(self):
        return self.__data

    def setData(self, value: any):
        self.__data = value

    def getNext(self):
        return self.__next

    def setNext(self, node):
        if isinstance(node, Node) or node is None:
            self.__next = node
        else:
            raise struture_exception.NodeTypeError(node)

    def __str__(self):
        return "(%s)" % str(self.__data)
