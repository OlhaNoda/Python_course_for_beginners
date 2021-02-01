import unittest
from function_example_for_task1 import make_operations


class MakeOperationsTestCase(unittest.TestCase):

    def test_addition(self):
        sum_value1 = make_operations('+', 6, 1, 3)
        sum_value2 = make_operations('+', -6, -1, 0, 1)
        sum_value3 = make_operations('+', 5)
        self.assertEqual(sum_value1, 10)
        self.assertEqual(sum_value2, -6)
        self.assertEqual(sum_value3, 5)

    def test_subtraction(self):
        diff_value1 = make_operations('-', 6, 1, 3)
        diff_value2 = make_operations('-', 0, 1, 3)
        diff_value3 = make_operations('-', -6, 1, 3)
        diff_value4 = make_operations('-', 5)
        self.assertEqual(diff_value1, 2)
        self.assertEqual(diff_value2, -4)
        self.assertEqual(diff_value3, -10)
        self.assertEqual(diff_value4, 5)

    def test_multiplication(self):
        prod_value1 = make_operations('*', 6, 1, -3)
        prod_value2 = make_operations('*', 1, 0, 3)
        prod_value3 = make_operations('*', 0)
        prod_value4 = make_operations('*', -2, -3)
        self.assertEqual(prod_value1, -18)
        self.assertEqual(prod_value2, 0)
        self.assertEqual(prod_value3, 0)
        self.assertEqual(prod_value4, 6)

    def test_operator(self):
        value = make_operations('!', 2, 3)
        self.assertEqual(value, False)

    def test_type(self):
        value = make_operations('+', 'r', 5)
        self.assertEqual(value, False)


if __name__ == "__main__":
    unittest.main()
