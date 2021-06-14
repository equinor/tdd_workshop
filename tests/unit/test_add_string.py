"""
Task
String calculation:
The method can take two numbers, separated by commas, and will return their sum.
For example "1,2" would return 3.

"""
import pytest
from operators.add_string import add_string


@pytest.mark.parametrize("input_data, expected", [("3,5", 8), ("2,4", 6), ("6,9", 15)])
def test_sum_numbers(input_data, expected):
    assert add_string(input_data) == expected
