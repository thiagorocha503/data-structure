import unittest
from queue_ import Queue_
from struture_exception import QueueError


class QueueTest(unittest.TestCase):

    def test_create(self):
        self.assertIsInstance(Queue_(), Queue_)

    def test_peek_last(self):
        queue = Queue_()
        self.assertRaises(QueueError, lambda: queue.peek())
        self.assertRaises(QueueError, lambda: queue.getLast())
        queue.enqueue(21)
        queue.enqueue(25)
        self.assertEqual(queue.peek(), 21)
        self.assertEqual(queue.getLast(), 25)

    def test_enqueue_dequeue(self):
        queue = Queue_()
        for j in range(1, 7):
            queue.enqueue(j)
        self.assertEqual(queue.findAll(), [1, 2, 3, 4, 5, 6])
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.getLast(), 6)
        for i in range(3):
            queue.dequeue()
        self.assertEqual(queue.findAll(), [4, 5, 6])
        self.assertEqual(queue.peek(), 4)
        self.assertEqual(queue.getLast(), 6)

    def test_findAll(self):
        queue = Queue_()
        self.assertEqual(queue.findAll(), [])
        for i in range(1, 7):
            queue.enqueue(i)
        self.assertEqual(queue.findAll(), [1, 2, 3, 4, 5, 6])
