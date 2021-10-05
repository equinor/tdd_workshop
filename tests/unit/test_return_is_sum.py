from operators.return_is_sum import return_is_sum
import pytest


@pytest.mark.parametrize(
    "string_input, target", [((1, 1), 2), ((-1, -1), -2), ((1, -1), 0)]
)
def test_return_is_sum(string_input, target):
    result = return_is_sum(string_input)
    assert result == target
