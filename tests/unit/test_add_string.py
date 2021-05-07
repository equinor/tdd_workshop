from operators.add_string import add_string
import pytest


@pytest.mark.parametrize("input, expected_result", [("1,2", 1 + 2), ("1", 1), ("", 0)])
def test_add_string(input, expected_result):
    result = add_string(input)
    assert expected_result == result
