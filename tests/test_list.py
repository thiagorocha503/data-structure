import unittest
from list_dynamic import ListDynamic
from struture_exception import ListDynamicIndexError


class ListDinamicTest(unittest.TestCase):

    def test_add_remove(self):
        lista = ListDynamic()
        self.assertEqual(lista.findAll(), [])
        self.assertEqual(lista.length(), 0)

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

    def test_clean_isEmtpty_length(self):
        lista: ListDynamic = ListDynamic()
        for i in range(1, 6):
            lista.add(i)
        self.assertEqual(lista.length(), 5)
        self.assertFalse(lista.isEmpty())
        lista.clean()
        self.assertEqual(lista.length(), 0)
        self.assertTrue(lista.isEmpty())

    def test__add__(self):
        list_a: ListDynamic = ListDynamic()
        for number in range(1, 6):
            list_a.add(number)
        self.assertEqual(list_a.findAll(), [1, 2, 3, 4, 5])

        list_b: ListDynamic = ListDynamic()
        for number in range(6, 11):
            list_b.add(number)
        self.assertEqual(list_b.findAll(), [6, 7, 8, 9, 10])

        list_x: ListDynamic = list_a + list_b
        self.assertEqual(list_x.findAll(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        # Remove elemento nas duas lista simples
        list_a.remove(3)
        list_b.remove(8)
        self.assertEqual(list_a.findAll(), [1, 2, 4, 5])
        self.assertEqual(list_b.findAll(), [6, 7, 9, 10])
        self.assertEqual(list_x.findAll(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_other(self):
        list_test: ListDynamic = ListDynamic()

        # Test lista vazia
        self.assertRaises(ListDynamicIndexError, list_test.get, 0)
        self.assertEqual(list_test.indexOf(10), -1)

        elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for e in elements:
            list_test.add(e)

        # Test indexOf
        for index in range(list_test.length()):
            self.assertEqual(list_test.indexOf(elements[index]), index, "index: %d, value: %s" % (index, elements[index]))
        # valores inexistente
        self.assertEqual(list_test.indexOf(-1), -1)
        self.assertEqual(list_test.indexOf(11), -1)

        # Test get
        for index in range(list_test.length()):
            self.assertEqual(list_test.get(index), elements[index], "index: %d, value: %s" % (index, elements[index]))
        # Test exception
        self.assertRaises(ListDynamicIndexError, list_test.get, -1)
        self.assertRaises(ListDynamicIndexError, list_test.get, 11)


if __name__ == "__main__":
    unittest.main()
