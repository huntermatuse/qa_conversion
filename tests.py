import pytest
import math_testing

class TestMathFunctions:
    def test_add(self):
        assert math_testing.add(1, 2) == 3

    def test_add_fail(self):
        assert not math_testing.add(2,2) == 5