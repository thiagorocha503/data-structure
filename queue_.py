import node
from struture_exception import QueueError


class Queue_:

    def __init__(self):
        self.__front = None  # inicio
        self.__rear = None  # fim

    def getLast(self):
        if self.__rear is None:
            raise QueueError("Fila vazia")
        else:
            return self.__rear.getData()

    def peek(self):
        if self.__front is None:
            raise QueueError("Fila vazia")
        else:
            return self.__front.getData()

    def enqueue(self, value):
        new_node = node.Node(value)
        if self.__front is None:
            self.__front = new_node
            self.__rear = new_node
        else:
            self.__rear.setNext(new_node)
            self.__rear = new_node

    def dequeue(self):
        if self.__front is None:
            raise QueueError("Fila vazia")
        else:
            if self.__front.getNext() is None:  # Fila com um unico elemento:
                self.clean()
                return True
            else:  # Fila de dois ou mais elemento
                new_start = self.__front.getNext()
                self.__front = new_start
            return True

    def clean(self):
        self.__front = None
        self.__rear = None

    def findAll(self):
        aux = self.__front
        nodes = []
        while aux is not None:
            nodes.append(aux.getData())
            aux = aux.getNext()
        return nodes

    # método alternativo ao enqueue
    def put(self, value):
        return self.enqueue(value)

    # método alternativo ao dequeue
    def get(self):
        return self.dequeue()

    def __str__(self):
        return str(self.findAll())
