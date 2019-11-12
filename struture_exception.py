class QueueError(Exception):

    def __init__(self, erro):
        self.erro = erro

    def __str__(self):
        return str(self.erro)


class NodeTypeError(Exception):

    def __init__(self, object_passado):
        self.object_passado = object_passado

    def __str__(self):
        return "Expected um Node object,  but received type<%s>" % str(type(self.object_passado))


class StackUnderflowError(Exception):

    def __str__(self):
        return "StackUnderflowError: A pilha está vazia"
