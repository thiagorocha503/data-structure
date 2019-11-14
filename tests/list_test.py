from listDinamic import ListDinamic
import unittest


class ListDinamicTest(unittest.TestCase):

    def test_create(self):
        self.assertTrue(isinstance(ListDinamic(), ListDinamic))
        self.assertEqual(ListDinamic().length(), 0)

    def test_add(self):
        lista = ListDinamic()
        self.assertEqual(lista.add(1), None)

    def test_remove(self):
        lista = ListDinamic()
        for i in range(1,  6):
            lista.add(i)
        self.assertEqual(lista.findAll(), [1, 2, 3, 4, 5])
        self.assertEqual(lista.length(), 5)

        # remover nó entre nós
        lista.remove(3)
        self.assertEqual(lista.findAll(), [1, 2, 4, 5])
        self.assertEqual(lista.length(), 4)

        # remover nó ínicial da lista
        lista.remove(1)
        self.assertEqual(lista.findAll(), [2, 4, 5])
        self.assertEqual(lista.length(), 3)

        # remover elemento no final da lista
        lista.remove(5)
        self.assertEqual(lista.findAll(), [2, 4])
        self.assertEqual(lista.length(), 2)

    def test_clean(self):
        lista = ListDinamic()
        for i in range(1, 6):
            lista.add(i)
        self.assertEqual(lista.length(), 5)
        lista.clean()
        self.assertEqual(lista.length(), 0)


if __name__ == "__main__":
    unittest.main()
