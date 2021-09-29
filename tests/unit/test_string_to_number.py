# Test with "", "-1", "1", "+1"
from operators.string_to_number import string_to_int


def test_string_to_int():
    string_input = "1"
    result = string_to_int(string_input)
    assert result == int("1")
