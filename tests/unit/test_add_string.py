"""
This suite tests the add_string method

"""
import pytest
from operators.add_string import add_string

@pytest.mark.parametrize("test_input, expected", 
    [("1,1", 2), ("2,2", 4), ("0,0", 0), ("1", 1), ("1,2,3", 6)]
    )
def test_add_string(test_input, expected):
    assert add_string(test_input) == expected

def test_add_string_raises_typeerror():
    """Assert that add_string raises error on erroneous input"""
    with pytest.raises(TypeError):
        add_string("a, b")

def test_add_string_typeerror_when_not_string():
    """Verify that add_string raises TypeError when non-string is given"""
    with pytest.raises(TypeError):
        add_string(1)

