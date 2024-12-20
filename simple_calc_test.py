import unittest
from tdd_simple_calculator import simple_calculator


class TestSimpleCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(simple_calculator("5+5"), 10)
        self.assertEqual(simple_calculator("10+20+30"), 60)

    def test_subtraction(self):
        self.assertEqual(simple_calculator("10-6"), 4)
        self.assertEqual(simple_calculator("50-20-10"), 20)

    def test_combined_operations(self):
        self.assertEqual(simple_calculator("1+2-4"), -1)
        self.assertEqual(simple_calculator("100-50+25"), 75)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            simple_calculator("5++5")
        with self.assertRaises(ValueError):
            simple_calculator("10-")
        with self.assertRaises(ValueError):
            simple_calculator("")


if __name__ == "__main__":
    unittest.main()


# Test cases
# if __name__ == "__main__":
#     # Valid cases
#     print(simple_calculator("5+5"))  # Expected: 10
#     print(simple_calculator("10-6"))  # Expected: 4
#     print(simple_calculator("1+2-4"))  # Expected: -1
#     print(simple_calculator("100-50+25"))  # Expected: 75
#
#     # Edge cases
#     print(simple_calculator("1000+1-1"))  # Expected: 1000
#     print(simple_calculator("1+1+1+1+1"))  # Expected: 5
#
#     # Invalid cases (should raise ValueError)
#     try:
#         print(simple_calculator("5++5"))  # Invalid: consecutive operators
#     except ValueError as e:
#         print(e)  # Expected: Invalid input expression
#
#     try:
#         print(simple_calculator("10-"))  # Invalid: ends with an operator
#     except ValueError as e:
#         print(e)  # Expected: Invalid input expression
#
#     try:
#         print(simple_calculator(""))  # Invalid: empty string
#     except ValueError as e:
#         print(e)  # Expected: Invalid input expression