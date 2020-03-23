import node
import struture_exception


class Stack:

    def __init__(self):
        self.__top = None

    def peek(self):
        if self.__top is None:
            raise struture_exception.StackUnderflowError
        else:
            return self.__top.getData()

    def push(self, value):
        new_node = node.Node(value)
        if self.__top is None:  # Pilha vazia
            self.__top = new_node
        else:  # pilha com dois ou mais elemento
            new_node.setNext(self.__top)
            self.__top = new_node

    def pop(self):
        if self.__top is None:
            raise struture_exception.StackUnderflowError
        else:
            pushed = self.__top.getData()
            self.__top = self.__top.getNext()
            return pushed

    def __str__(self):
        return str(self.findAll())

    def findAll(self):
        if self.__top is None:
            return []
        else:
            nodes = []
            aux = self.__top
            while aux is not None:
                nodes.append(aux.getData())
                aux = aux.getNext()
            return nodes

    def clean(self):
        self.__top = None

    def isEmpty(self):
        if self.__top is None:
            return True
        else:
            return False
