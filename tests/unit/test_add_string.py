from operators.add_string import string_add
import pytest


@pytest.mark.parametrize(
    "string_input, target", [("1,2", 3), ("-1,2", 1), ("0,0", 0), ("1.5,2.5", 4)]
)
def test_two_string_numbers_are_added(string_input, target):
    assert string_add(string_input) == target


@pytest.mark.parametrize("string_input", [("1,2,3"), ("-1"), ("a,b"), (","), ("")])
def test_invalid_input_gives_valueerror(string_input):
    with pytest.raises(ValueError):
        string_add(string_input)
