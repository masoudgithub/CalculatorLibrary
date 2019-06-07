"""
Unit test for the calculator library
"""

import calculator


class TestCalculator:

    def test_additoin(self):
        assert 4 == calculator.add(2, 2)

    def test_subtractoin(self):
        assert 2 == calculator.subtract(4, 2)
