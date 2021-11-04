from operators.sum_numbers_in_string import *
import pytest

def test_sum_numbers_in_string():
    string_input = "1,2"
    result = sum_numbers_in_string(string_input)
    assert result==3

def test_empty_string():
    string_input = ""
    with pytest.raises(ValueError):
        sum_numbers_in_string(string_input)

def test_none_input():
    string_input = None
    with pytest.raises(AttributeError):
        sum_numbers_in_string(string_input)

def test_sum_1_numbers_comma_in_string():
    string_input = "1,"
    with pytest.raises(ValueError):
        sum_numbers_in_string(string_input)

def test_sum_1_numbers_in_string():
    string_input = "1"
    with pytest.raises(ValueError):
        sum_numbers_in_string(string_input)

def test_sum_too_many_numbers():
    string_input = "1,2,3"
    with pytest.raises(ValueError):
        sum_numbers_in_string(string_input)

def test_sum_too_many_commas():
    string_input = "1,2,"
    with pytest.raises(ValueError):
        sum_numbers_in_string(string_input)