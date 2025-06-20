import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        # Basic positive numbers
        self.assertEqual(self.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 5), 15)
        
        # Adding negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)
        
        # Adding zero
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, -3), -3)
        
        # Adding decimals
        self.assertEqual(self.calc.add(2.5, 3.7), 6.2)
        self.assertEqual(self.calc.add(-1.5, 2.5), 1.0)

    def test_subtraction(self):
        """Test the subtraction method."""
        # Basic subtraction
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(3, 2), 1)
        
        # Subtracting negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(5, -3), 8)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        
        # Subtracting zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        
        # Subtracting decimals
        self.assertEqual(self.calc.subtract(5.5, 2.2), 3.3)
        self.assertEqual(self.calc.subtract(-1.5, 2.5), -4.0)

    def test_multiplication(self):
        """Test the multiplication method."""
        # Basic multiplication
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(7, 2), 14)
        
        # Multiplying with negative numbers
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        self.assertEqual(self.calc.multiply(5, -2), -10)
        
        # Multiplying with zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        
        # Multiplying with one
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.multiply(1, -3), -3)
        
        # Multiplying decimals
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(-1.5, 2), -3.0)

    def test_division(self):
        """Test the division method."""
        # Basic division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        
        # Division with negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        
        # Division resulting in zero
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -3), 0.0)
        
        # Division by zero - should return None
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        
        # Division with decimals
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertEqual(self.calc.divide(-6.6, 2.2), -3.0)
        
        # Division by one
        self.assertEqual(self.calc.divide(5, 1), 5.0)
        self.assertEqual(self.calc.divide(-3, 1), -3.0)

if __name__ == "__main__":
    unittest.main()
