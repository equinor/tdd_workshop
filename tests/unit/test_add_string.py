"""
Task 1
String calculation:
The method can take two numbers, separated by commas, and will return their sum.
For example "1,2" would return 3.

Task 2
The method can take up to two numbers, separated by commas, and will return their sum.
For example "" or "1", where an empty string will return 0.
"""
import pytest
from operators.add_string import add_string


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("3,5", 8),
        ("-2,4", 2),
        ("6,9", 15),
        ("3+1j,9", 12+1j),
        ("", 0),
        ("1", 1),
        pytest.param("3,5", 10, marks=pytest.mark.xfail(
            strict=True,
            reason='incorrect sum')),
    ])
def test_sum_numbers(input_data, expected):
    assert add_string(input_data) == expected
