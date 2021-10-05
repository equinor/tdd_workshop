from operators.add_string import add_string
import pytest


@pytest.mark.parametrize(
    "string_input, target", [("1,2", 3), ("-1,1", 0), ("-1,-2", -3), ("0,1", 1)]
)
def test_add_string(string_input, target):
    result = add_string(string_input)
    assert result == target
