""" Create unit tests for a program, unittest_example.py 
		All test should pass.

    Run the tests:
    $ python unitest_example.py
"""
import unittest

# Function to be tested
def add(a, b):
    return a + b

# Define test cases
class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)
    
    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
    
    def test_add_positive_and_negative(self):
        self.assertEqual(add(1, -1), 0)

    def test_fail(self):
        self.assertNotEqual(add(1, 1), 3)

# Run the tests
if __name__ == '__main__':
    unittest.main() # use if running in a python script

