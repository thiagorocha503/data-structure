from node import Node
from struture_exception import ListDynamicIndexError, StrutureTypeExcption


class ListDynamic:

    def __init__(self):
        self.__node: Node or None = None
        self.__length: int = 0
        self.__currentIndex: int = 0

    def add(self, value: any) -> None:
        self.__length += 1
        if self.__node is None:
            self.__node = Node(value)
        else:
            self.__add(value, self.__node)

    def __add(self, value: any, node: Node):
        if node.getNext() is None:
            node.setNext(Node(value))
        else:
            self.__add(value, node.getNext())

    def remove(self, value: any) -> None:
        if self.__node is None:
            return
        if self.__node.getInfo() == value:
            self.__node = self.__node.getNext()
            self.__length -= 1
            return
        self.__remove(value, self.__node)

    def __remove(self, value: any, node: Node):
        # Verifica apenas um nó a frente
        if node.getNext() is not None:
            if node.getNext().getInfo() == value:
                node.setNext(node.getNext().getNext())
                self.__length -= 1
            else:
                self.__remove(value, node.getNext())
        else:
            return

    def indexOf(self, value: any) -> int:
        currentNode: Node = self.__node
        for index in range(self.__length):
            if currentNode.getInfo() == value:
                return index
            currentNode = currentNode.getNext()
        return -1

    def get(self, index: int) -> any:
        return self.__get(index).getInfo()

    def __get(self, key: int) -> Node:
        if key > self.__length - 1 or key < 0:
            raise ListDynamicIndexError(key)
        currentNode: Node = self.__node
        for i in range(key):
            currentNode = currentNode.getNext()
        if currentNode is None:
            raise ListDynamicIndexError(key)
        return currentNode

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

    # Métodos especias
    def __str__(self) -> str:
        return str(self.findAll())

    def __add__(self, other):
        if not isinstance(other, ListDynamic):
            raise StrutureTypeExcption("%s is not type ListDynamic" % other)
        new_list_dynamic: ListDynamic = ListDynamic()
        for e in self.findAll():
            new_list_dynamic.add(e)
        for e in other.findAll():
            new_list_dynamic.add(e)
        return new_list_dynamic

    def __len__(self) -> int:
        return self.length()

    def __getitem__(self, key: int) -> any:
        return self.__get(key).getInfo()

    def __setitem__(self, key: int, value: any) -> any:
        currentNode: Node = self.__get(key)
        currentNode.setInfo(value)

    def __eq__(self, other) -> bool:
        if not isinstance(other, ListDynamic):
            raise StrutureTypeExcption("%s is not type ListDynamic" % other)
        if len(other) != len(self):
            return False
        for i in range(self.length()):
            if self.get(i) != other.get(i):
                return False
        return True

    def __ne__(self, other) -> bool:
        if not isinstance(other, ListDynamic):
            raise StrutureTypeExcption("%s is not type ListDynamic" % other)
        if self.__eq__(other):
            return False
        else:
            return True

    def __iter__(self):
        return self

    def __next__(self):
        if self.__currentIndex < self.__length:
            result = self.get(self.__currentIndex)
            self.__currentIndex += 1
            return result
        else:
            self.__currentIndex = 0
            raise StopIteration
