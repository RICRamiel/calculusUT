import sys
import unittest
from main import Calculus, History


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.history = History()
        self.calculator = Calculus()

    def tearDown(self):
        print(*self.calculator.history.data)

    def test_sum(self):
        self.assertEqual(self.calculator.sum(2, 3), 5)
        self.assertEqual(self.calculator.sum(-1, 1), 0)
        self.assertEqual(self.calculator.sum(0, 0), 0)
        self.assertEqual(self.calculator.sum(-10, -10), -20)
        self.assertEqual(self.calculator.sum(-7, 5), -2)
        self.assertEqual(self.calculator.sum(0.1, 5), 5.1)

    def test_very_big(self):
        self.assertEqual(self.calculator.sum(sys.maxsize * 5, 10), sys.maxsize * 5 + 10)

    def test_very_very_big(self):
        self.assertEqual(self.calculator.sum(2 ^ 64, 2 ^ 64), 2 ^ 64 * 2)

    def test_history_store(self):
        self.calculator.sum(2, 3)
        self.assertEqual(self.calculator.history.data, [(2, 3, 5)])

        self.calculator.sum(-1, 1)
        self.assertEqual(self.calculator.history.data, [(2, 3, 5), (-1, 1, 0)])


if __name__ == '__main__':
    unittest.main()
