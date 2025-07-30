import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Comprehensive unit tests for SimpleCalculator class."""
    
    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()
    
    # Addition tests
    def test_addition_positive(self):
        self.assertEqual(self.calc.add(2, 3), 5)
    
    def test_addition_negative(self):
        self.assertEqual(self.calc.add(-1, -1), -2)
    
    def test_addition_mixed_signs(self):
        self.assertEqual(self.calc.add(5, -3), 2)
    
    def test_addition_zero(self):
        self.assertEqual(self.calc.add(0, 7), 7)
        self.assertEqual(self.calc.add(4, 0), 4)
    
    # Subtraction tests
    def test_subtraction_positive(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
    
    def test_subtraction_negative(self):
        self.assertEqual(self.calc.subtract(-1, -1), 0)
    
    def test_subtraction_mixed_signs(self):
        self.assertEqual(self.calc.subtract(10, -5), 15)
    
    def test_subtraction_zero(self):
        self.assertEqual(self.calc.subtract(7, 0), 7)
        self.assertEqual(self.calc.subtract(0, 4), -4)
    
    # Multiplication tests
    def test_multiplication_positive(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
    
    def test_multiplication_negative(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)
    
    def test_multiplication_mixed_signs(self):
        self.assertEqual(self.calc.multiply(5, -2), -10)
    
    def test_multiplication_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(3, 0), 0)
    
    # Division tests
    def test_division_positive(self):
        self.assertAlmostEqual(self.calc.divide(10, 2), 5.0)
    
    def test_division_negative(self):
        self.assertAlmostEqual(self.calc.divide(-9, -3), 3.0)
    
    def test_division_mixed_signs(self):
        self.assertAlmostEqual(self.calc.divide(15, -3), -5.0)
    
    def test_division_fraction(self):
        self.assertAlmostEqual(self.calc.divide(1, 2), 0.5)
    
    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))
    
    def test_division_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0.0)

if __name__ == '__main__':
    unittest.main()
