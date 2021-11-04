# Test with "", "-1", "1", "+1"

from operators.string_to_number import string_to_int

import pytest

def test_empty_to_int():
    string_input = ""
    with pytest.raises(ValueError, match="Converting string"):
        string_to_int(string_input)

def test_string_to_int():
    string_input = "1"
    result = string_to_int(string_input)
    assert result == 1


