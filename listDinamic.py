from node import Node


class ListDinamic:

    def __init__(self):
        self.__node = None
        self.__length = 0

    def length(self):
        return self.__length

    def add(self, value):
        if self.__node is None:
            self.__node = Node(value)
        else:
            self.__node.add(value)
        self.__length += 1

    def remove(self, value):
        if self.__node.getInfo() == value:
            self.__node = self.__node.getNext()
            self.__length -= 1
            return True
        removed = self.__node.remove(value)
        if removed:
            self.__length -= 1
            return True
        else:
            return False

    def clean(self):
        self.__node = None
        self.__length = 0

    def findAll(self):
        return self.__node.findAll()

    def find(self, value):
        return self.__node.find(value)

    def __str__(self):
        return str(self.findAll())
