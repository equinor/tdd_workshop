import pytest
from operators.add_string import add_string


def test_add_empty_string_equals_zero():
    assert add_string("") == 0


def test_add_ond_equals_one():
    assert add_string("1") == 1


def test_add_one_and_two_equals_three():
    assert add_string("1,2") == 3


def test_add_two_and_two_equals_four():
    assert add_string("2,2") == 4


def test_add_one_two_and_three_equals_six():
    assert add_string("1,2,3") == 6


def test_spaces_in_input():
    assert add_string("1 ,2") == 3


def test_newlines_in_input():
    assert add_string("1\n2,3") == 6


def test_raises_exception_on_illegal_newline_input():
    with pytest.raises(ValueError):
        add_string("1,\n")
