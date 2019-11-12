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
        if self.__next is None:
            self.__next = Node(value)
        else:
            return self.__next.add(self.__next)

    def remove(self, value):
        if self.__info == value:  # encontrou
            self.__next = Node(value)
        else:
            if self.__next is None:  # fim da lista
                return False
            else:
                return self.__next.remove(value)

    def __str__(self):
        return "[%s]" % str(self.__info)
