from node import Node
from struture_exception import NodeTypeError
import unittest


class NodeTest(unittest.TestCase):

    def test_gettters_setteres(self):
        # No com valor inicial
        node_ = Node(7)
        self.assertEqual(node_.getInfo(), 7)
        self.assertIsNone(node_.getNext())

        # Nó sem valor inicial
        node_a: Node = Node()
        self.assertEqual(node_a.getInfo(), None)
        self.assertEqual(node_a.getNext(), None)

        node_a.setInfo(5)
        node_b: Node = Node(9)
        node_a.setNext(node_b)
        self.assertEqual(node_a.getInfo(), 5)
        self.assertEqual(node_a.getNext(), node_b)
        self.assertEqual(node_a.getNext().getInfo(), 9)
        self.assertEqual(node_a.getNext().getNext(), None)

        #  test Exception
        self.assertRaises(NodeTypeError, lambda: Node(2, object))
        self.assertRaises(NodeTypeError, lambda: node_a.setNext(object))


if __name__ == "__main__":
    unittest.main()
