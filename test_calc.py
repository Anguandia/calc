"""Unit tests for the calculator library."""

import calc


class TestCalculator:

    def test_addition(self):
        assert calc.add(2, 2) == 4

    def test_subtraction(self):
        assert calc.subtract(4, 2) == 2

    def test_multiplication(self):
        assert calc.multiply(10, 10) == 100

    def test_division(self):
        assert calc.divide(10, 2) == 5

    def test_exp(self):
        assert calc.exp(3, 4) == 81
