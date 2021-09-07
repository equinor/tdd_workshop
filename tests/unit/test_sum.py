from operators.sum_two_numbers import sum_two_numbers
import pytest


@pytest.mark.parametrize("number1, number2, expected", [(1, 2, 3), (2, 2, 4)])
def test_sum_of_two_numbers(number1, number2, expected):
    result = sum_two_numbers(number1, number2)
    assert expected == result
