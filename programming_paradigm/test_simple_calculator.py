import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---------- ADDITION TESTS ----------
    def test_addition_integers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_addition_floats(self):
        self.assertAlmostEqual(self.calc.add(2.5, 1.2), 3.7, places=7)
        self.assertAlmostEqual(self.calc.add(-1.5, 1.5), 0.0, places=7)

    def test_addition_large_numbers(self):
        self.assertEqual(self.calc.add(10**12, 10**12), 2 * 10**12)

    # ---------- SUBTRACTION TESTS ----------
    def test_subtraction_integers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(4, 10), -6)

    def test_subtraction_with_negatives(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-5, 3), -8)

    def test_subtraction_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3, places=7)

    # ---------- MULTIPLICATION TESTS ----------
    def test_multiplication_integers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 4), -8)

    def test_multiplication_by_zero(self):
        self.assertEqual(self.calc.multiply(12345, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_multiplication_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0, places=7)

    # ---------- DIVISION TESTS ----------
    def test_division_integers(self):
        self.assertAlmostEqual(self.calc.divide(10, 2), 5.0, places=7)
        self.assertAlmostEqual(self.calc.divide(-9, 3), -3.0, places=7)

    def test_division_floats(self):
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0, places=7)
        self.assertAlmostEqual(self.calc.divide(1, 3), 1.0 / 3.0, places=7)

    def test_division_by_zero_returns_none(self):
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_division_precision(self):
        # Check precision for a non-terminating decimal
        result = self.calc.divide(10, 3)
        self.assertAlmostEqual(result, 10.0 / 3.0, places=7)

    # ---------- PROPERTIES / RELATIONS ----------
    def test_addition_commutativity(self):
        self.assertEqual(self.calc.add(7, 2), self.calc.add(2, 7))

    def test_multiplication_commutativity(self):
        self.assertEqual(self.calc.multiply(6, 9), self.calc.multiply(9, 6))

    def test_subtract_not_commutative(self):
        # Confirm subtraction is not commutative
        self.assertNotEqual(self.calc.subtract(5, 2), self.calc.subtract(2, 5))

    # ---------- TYPE BEHAVIOR (basic) ----------
    def test_operations_with_int_and_float_mix(self):
        self.assertAlmostEqual(self.calc.add(2, 2.5), 4.5, places=7)
        self.assertAlmostEqual(self.calc.multiply(3, 2.5), 7.5, places=7)
        self.assertAlmostEqual(self.calc.subtract(5, 2.5), 2.5, places=7)
        self.assertAlmostEqual(self.calc.divide(5, 2.0), 2.5, places=7)


if __name__ == "__main__":
    unittest.main()
