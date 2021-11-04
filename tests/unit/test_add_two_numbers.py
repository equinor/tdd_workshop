from operators.add_two_numbers import add_two_numbers

import pytest

def test_add_two_numbers_test1():
    string_input = "1,2"
    result = add_two_numbers(string_input)
    assert result == 3

def test_add_two_numbers_test2():
    string_input = "2,2"
    result = add_two_numbers(string_input)
    assert result == 4  

