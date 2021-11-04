# Test with "", "-1", "1", "+1"
from operators.string_to_number import string_to_int


def test_string_to_int():
    string_input = "1"
    result = string_to_int(string_input)
    assert result == 1


import pytest

def test_two_numbers_in_string():
    string_input = "1,2"
    result = string_to_int(string_input)
    assert result == 3
    
def test_multiple_numbers_in_string():
    string_input = "1,2,3,4"
    result = string_to_int(string_input)
    assert result == 10

def test_empty_to_int():
    string_input = ""
    with pytest.raises(ValueError, match = "Converting string to integer failed"):
        string_to_int(string_input)


def test_minus_to_int():
    string_input = "-1"
    result = string_to_int(string_input)
    assert result == -1

def test_plus_to_int():
    string_input = "+1"
    result = string_to_int(string_input)
    assert result == 1

def test_mixed_delimiter_in_string():
    string_input = "1.2,3-4"
    result = string_to_int(string_input)
    assert result == 10