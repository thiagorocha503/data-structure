import unittest
from stack import *
from struture_exception import StackUnderflowError


class StackTest(unittest.TestCase):

    def test_pop_push_peek(self):
        #  pilha iniciada
        p = Stack()
        self.assertEqual(p.findAll(), [])
        #   Stack
        #
        #    | |
        #    |_|
        #
        self.assertRaises(StackUnderflowError, p.peek)
        p.push(1)
        #   Stack
        #
        #    |1|
        p.push(2)
        #    Stack
        #
        #    |2|
        #    |1|
        #
        assert p.peek() == 2
        assert p.findAll() == [2, 1]

        p.push(3)
        #    Stack
        #
        #    |3|
        #    |2|
        #    |1|
        #
        self.assertEqual(p.peek(), 3)
        self.assertEqual(p.findAll(), [3, 2, 1])

        self.assertEqual(p.pop(), 3)
        #    Stack
        #
        #    | |
        #    |2|
        #    |1|
        #
        self.assertEqual(p.peek(), 2)
        self.assertEqual(p.findAll(), [2, 1])

        for i in range(4, 6):
            p.push(i)
        #    Stack
        #
        #    | |
        #    |5|
        #    |4|
        #    |2|
        #    |1|
        #
        self.assertEqual(p.peek(), 5)
        self.assertEqual(p.findAll(), [5, 4, 2, 1])

        self.assertEqual(p.pop(), 5)
        self.assertEqual(p.pop(), 4)

        p.clean()
        self.assertTrue(p.isEmpty())
        self.assertRaises(StackUnderflowError, p.pop)

    def test_findAll(self):
        stack = Stack()
        for i in (2, 3, 5, 7, 11):
            stack.push(i)
        self.assertEqual(stack.findAll(), [11, 7, 5, 3, 2])

    def test_isEmpty(self):
        stack = Stack()
        for j in (2, 3, 5, 7, 11):
            stack.push(j)
        self.assertFalse(stack.isEmpty())
        stack.clean()
        self.assertTrue(stack.isEmpty())


if __name__ == "__main__":
    unittest.main()

