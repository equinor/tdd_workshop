# Test with "", "-1", "1", "+1"
from operators.string_to_number import string_to_int
import pytest


@pytest.mark.parametrize(
    "string_input, expected_result", [("", 0), ("1", 1), ("-1", -1), ("+1", 1)]
)
def test_string_to_int(string_input, expected_result):
    result = string_to_int(string_input)
    assert result == expected_result
