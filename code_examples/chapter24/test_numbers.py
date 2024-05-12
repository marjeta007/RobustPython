import unittest

from code_examples.chapter24.numbers import add


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_add(self):
        first = 20
        second = 22
        expected = 42
        actual = add(first, second)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
