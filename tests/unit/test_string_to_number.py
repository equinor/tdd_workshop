# Test with "", "-1", "1", "+1"
from operators.string_to_number import string_to_int

import pytest


@pytest.mark.parametrize("input_string, expected", [("1", 1), ("-1", -1), ("+1", 1)])
def test_string_to_int(input_string, expected):
    result = string_to_int(input_string)
    assert result == expected
