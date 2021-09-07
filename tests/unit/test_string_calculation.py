import pytest
from operators.string_calculation import string_calculation


@pytest.mark.parametrize(
    "string_input, expected_result", [("1,2", 3), ("1,1", 2), ("1.3, 2.8", 4.1)]
)
def test_string_calculation(string_input, expected_result):
    result = string_calculation(string_input)
    assert result == expected_result
