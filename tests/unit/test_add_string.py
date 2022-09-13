from re import X
from operators.add_string import add

def test_two_numbers_are_equal():
    assert 1 == 1

def test_string_to_int_added():
    assert add("1,2") == 3