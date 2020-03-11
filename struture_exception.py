class ListDynamicIndexError(Exception):

    def __init__(self, index: int):
        self.__index: int = index

    def __str__(self):
        return "Index <%d> out of range" % self.__index


class QueueError(Exception):

    def __init__(self, erro):
        self.erro = erro

    def __str__(self):
        return str(self.erro)


class NodeTypeError(Exception):

    def __init__(self, object_passado):
        self.object_passado = object_passado

    def __str__(self):
        return "Expected Node object, but received type<%s>" % str(type(self.object_passado))


class StackUnderflowError(Exception):

    def __str__(self):
        return "StackUnderflowError: Stack is empty"
