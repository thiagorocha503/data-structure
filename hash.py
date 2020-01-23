from listDinamic import ListDinamic

class HashTable:

    def __init__(self, size):
        self.table: list = []
        self.size = size
        for i in range(size):
            self.table.append(None)

    def isHashValido(self, hash):
        if hash >= 0 and hash < self.size:
            return True
        else:
            return False

    def insert(self, hash, value):
        if not self.isHashValido(hash):
            print("Index inválido: ", str(hash))
            return None
        if self.table[hash] is None:
            lista = ListDinamic()
            lista.add(value)
            self.table[hash] = lista
        else:
            self.table[hash].add(value)

    def search(self, hash, value):
        if not self.isHashValido(hash):
            print("Index inválido: ", str(hash))
            return None
        if self.table[hash] is None:
            return None
        else:
            pass




h = HashTable(3)
h.insert(0, "thiago")
h.insert(1, "Rocha")
h.insert(2, "ferreira")
print("=======")
print("0 ", h.table[0])
print("1 ",h.table[1])
print("2 ",h.table[2])
print("=======")
h.insert(2, "@")
h.insert(2, "@")
print("=======")
print("0 ", h.table[0])
print("1 ", h.table[1])
print("2 ", h.table[2])
print("- ", h.search(2, "@"))
