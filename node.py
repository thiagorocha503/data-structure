import struture_exception


class Node:

    def __init__(self, info, next_=None):
        self.__info = info
        self.__next = self.setNext(next_)

    def getInfo(self):
        return self.__info

    def setInfo(self, value):
        self.__info = value

    def getNext(self):
        return self.__next

    def setNext(self, next_):
        if isinstance(next_, Node) or next_ is None:
            self.__next = next_
        else:
            raise struture_exception.NodeTypeError(next_)

    def add(self, value):
        if self.__info is None:
            self.__info = value
        if self.__next is None:
            self.__next = Node(value)
        else:
            return self.__next.add(value)

    def remove(self, value):
        # não verifica o valor nó inicial
        if self.__next is not None:
            if self.__next.getInfo() == value:
                if self.__next.getNext() is None:# A -> B ==> A
                    self.__next = None
                else: # A -> B -> C ==> A -> B
                    self.__next = self.__next.getNext()
                return True
            else:
                return self.__next.remove(value)
        else:
            return False

    def findAll(self):
        nodes = [self.__info]
        next_node = self.__next
        while next_node is not None:
            nodes.append(next_node.getInfo())
            next_node = next_node.getNext()
        return nodes

    def __str__(self):
        return "[%s]" % str(self.__info)
