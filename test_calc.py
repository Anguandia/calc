"""
Unit tests for the calculator library
"""

import calc


class TestCalculator:

    def test_addition(self):
        assert calc.add(2, 2) == 4

    def test_subtraction(self):
        assert calc.subtract(4, 2) == 2

    def test_multiplication(self):
        assert calc.multiply(10, 10) == 100
