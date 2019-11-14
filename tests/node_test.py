from node import Node
from struture_exception import NodeTypeError
import unittest


class NodeTest(unittest.TestCase):

    def test_criacao(self):
        self.assertTrue(isinstance(Node(5), Node))
        node = Node(5)
        self.assertTrue(isinstance(Node(5, node), Node))
        self.assertRaises(NodeTypeError, lambda: Node(4, " "))

    def test_getters_setteres(self):
        node = Node(2)
        self.assertEqual(node.getInfo(), 2)
        self.assertEqual(node.getNext(), None)

        node.setInfo(3)
        next_node = Node(5)
        node.setNext(next_node)
        self.assertEqual(node.getInfo(), 3)
        self.assertTrue(isinstance(node.getNext(), Node))
        self.assertEqual(node.getNext(), next_node)
        self.assertRaises(NodeTypeError, lambda: node.setNext(3))

    def test_add(self):
        node = Node()
        node.add(1)
        self.assertEqual(node.findAll(),[1])
        for i in range(2, 6):
            node.add(i)
        self.assertEqual(node.findAll(), [1, 2, 3, 4, 5])
