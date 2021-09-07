# Test with "", "-1", "1", "+1"
import pytest
from operators.string_to_number import string_to_int


@pytest.mark.parametrize(
    "string_input, expected_result", [("1", 1), ("-1", -1), ("", 0)]
)
def test_string_to_int(string_input, expected_result):
    result = string_to_int(string_input)
    assert result == expected_result
