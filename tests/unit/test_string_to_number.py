# Test with "", "-1", "1", "+1"

import pytest
from operators.string_to_number import string_to_int
from operators.string_to_number import string_to_numbers


def test_string_to_int():
    string_input = "1"
    result = string_to_int(string_input)
    assert result == 1


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (("1,1"), (1, 1)),
        (("2,2", (2, 2))),
        (("-1,0", (-1, 0))),
        (("1"), (1,)),
        (("1,2,3"), (1, 2, 3)),
    ],
)
def test_string_to_numbers(test_input, expected):
    assert string_to_numbers(test_input) == expected


def test_string_to_numbers_typerror():
    with pytest.raises(TypeError):
        string_to_numbers(("a,b"))
