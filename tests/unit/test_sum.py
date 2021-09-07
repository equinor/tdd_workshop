from operators.sum_two_numbers import sum_two_numbers
import pytest


@pytest.mark.parametrize("numbers, expected", [("1, 2", 3), ("2, 2", 4)])
def test_sum_of_two_numbers(numbers, expected):
    result = sum_two_numbers(numbers)
    assert expected == result
