import unittest
from list_dynamic import ListDynamic
from struture_exception import ListDynamicIndexError, StrutureTypeExcption


class ListDinamicTest(unittest.TestCase):

    def test_add_remove(self):
        lista = ListDynamic()
        self.assertEqual(lista.findAll(), [])
        self.assertEqual(lista.length(), 0)
        self.assertEqual(len(lista), 0)

        for i in range(1,  6):
            lista.add(i)
        self.assertEqual(lista.findAll(), [1, 2, 3, 4, 5])
        self.assertEqual(lista.length(), 5)
        self.assertEqual(len(lista), 5)

        # remover nó entre nós
        lista.remove(3)
        self.assertEqual(lista.findAll(), [1, 2, 4, 5])
        self.assertEqual(lista.length(), 4)
        self.assertEqual(len(lista), 4)

        # remover nó ínicial da lista
        lista.remove(1)
        self.assertEqual(lista.findAll(), [2, 4, 5])
        self.assertEqual(lista.length(), 3)

        # remover elemento no final da lista
        lista.remove(5)
        self.assertEqual(lista.findAll(), [2, 4])
        self.assertEqual(lista.length(), 2)
        self.assertEqual(len(lista), 2)

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

        # test exception
        self.assertRaises(StrutureTypeExcption, list_a.__add__, 3.1415)  # list + 1

    def test_indexOf_get(self):
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

    def test_comparation(self):
        list_a: ListDynamic = ListDynamic()
        list_b: ListDynamic = ListDynamic()

        self.assertTrue(list_a == list_b)
        self.assertFalse(list_a != list_b)

        for i in range(1, 4):
            list_a.add(i)
            list_b.add(i)
        list_b.add(4)
        list_b.add(5)

        self.assertEqual(list_a.findAll(), [1, 2, 3])
        self.assertEqual(list_b.findAll(), [1, 2, 3, 4, 5])

        self.assertFalse(list_a == list_b)
        self.assertTrue(list_a != list_b)

        list_b.remove(5)
        list_b.remove(4)

        self.assertTrue(list_b == list_a)
        self.assertFalse(list_a != list_b)

        list_b.remove(3)
        self.assertFalse(list_a == list_b)
        self.assertTrue(list_a != list_b)

        #  --------------------------------
        list_x: ListDynamic = ListDynamic()
        list_x.add(1)
        list_x.add(2)
        list_y: ListDynamic = ListDynamic()
        list_y.add(1)
        list_y.add(2)
        list_z: ListDynamic = ListDynamic()
        list_z.add(2)
        list_z.add(1)

        # [1, 2] == [1, 2]
        # [1, 2] != [2, 1]

        self.assertTrue(list_x == list_y)
        self.assertFalse(list_x == list_z)

        self.assertFalse(list_x != list_y)
        self.assertTrue(list_x != list_z)

        # test exception
        self.assertRaises(StrutureTypeExcption,  list_x.__eq__, "a")  # list_x == "a"
        self.assertRaises(StrutureTypeExcption,  list_x.__ne__, "a")  # list_x != "a"

    def test_set_get_item(self):
        list_demo: ListDynamic = ListDynamic()
        numbers: list = [1, 2, 3, 4, 5]
        for i in numbers:
            list_demo.add(i)
        # test get
        for i in range(len(list_demo)):
            self.assertEqual(list_demo[i], numbers[i])

        # test set
        list_demo[0] = 8
        self.assertEqual(list_demo[0], 8)

        list_demo[2] = 9
        self.assertEqual(list_demo[2], 9)

        list_demo[3] = 7
        self.assertEqual(list_demo[3], 7)

    def test_iterator(self):
        lista: ListDynamic = ListDynamic()
        values: list = list(range(11))
        for i in values:
            lista.add(i)
        for j, e in enumerate(lista):
            self.assertEqual(e, values[j])


if __name__ == "__main__":
    unittest.main()
