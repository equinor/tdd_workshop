# Test with "", "-1", "1", "+1"
from operators.string_to_number import string_to_int
import pytest

@pytest.mark.parametrize("string_input, target", [("1", 1), ("-1", -1), ("", 0)])
def test_string_to_int(string_input, target):
    result = string_to_int(string_input)
    assert result == target