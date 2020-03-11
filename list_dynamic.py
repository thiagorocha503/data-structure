from node import Node
from struture_exception import ListDynamicIndexError


class ListDynamic:

    def __init__(self):
        self.__node: Node or None = None
        self.__length: int = 0

    def add(self, value) -> None:
        self.__length += 1
        if self.__node is None:
            self.__node = Node(value)
        else:
            self.__add(value, self.__node)

    def __add(self, value, node: Node):
        if node.getNext() is None:
            node.setNext(Node(value))
        else:
            self.__add(value, node.getNext())

    def remove(self, value) -> None:
        if self.__node is None:
            return
        if self.__node.getInfo() == value:
            self.__node = self.__node.getNext()
            self.__length -= 1
            return
        self.__remove(value, self.__node)

    def __remove(self, value, node: Node):
        # Verifica apenas um nó a frente
        if node.getNext() is not None:
            if node.getNext().getInfo() == value:
                node.setNext(node.getNext().getNext())
                self.__length -= 1
            else:
                self.__remove(value, node.getNext())
        else:
            return

    def indexOf(self, value) -> int:
        currentNode: Node = self.__node
        for index in range(self.__length):
            if currentNode.getInfo() == value:
                return index
            currentNode = currentNode.getNext()
        return -1

    def get(self, index: int):
        if index > self.__length - 1 or index < 0:
            raise ListDynamicIndexError(index)
        currentNode: Node = self.__node
        for i in range(index):
            currentNode = currentNode.getNext()
        if currentNode is None:
            raise ListDynamicIndexError(index)
        return currentNode.getInfo()

    def findAll(self) -> list:
        currentNode: Node = self.__node
        result: list = []
        while currentNode is not None:
            result.append(currentNode.getInfo())
            currentNode = currentNode.getNext()
        return result

    def length(self) -> int:
        return self.__length

    def isEmpty(self) -> bool:
        if self.__node is None:
            return True
        else:
            return False

    def clean(self) -> None:
        self.__node = None
        self.__length = 0

    def __str__(self) -> str:
        return str(self.findAll())

    def __add__(self, other_list):
        new_list_dynamic: ListDynamic = ListDynamic()
        for e in self.findAll():
            new_list_dynamic.add(e)
        for e in other_list.findAll():
            new_list_dynamic.add(e)
        return new_list_dynamic
