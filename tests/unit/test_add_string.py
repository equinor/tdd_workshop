from operators.add_string import add_string
import pytest

def test_add_two_numbers_in_string():
    assert add_string('1,2') == 3
    assert add_string('+2,2') == 4
    assert add_string('-2,+2') == 0

def test_empty_string():
    assert add_string('') == 0

@pytest.mark.parametrize('value,expected', [('1',1), ('1234',1234),('1,2,3',6)])
def test_add_string_commas(value, expected):
    assert add_string(value) == expected

def test_add_string_newline():
    assert add_string('1\n2') == 3

def test_add_string_comma_and_newline():
    assert add_string('1\n2,3') == 6

@pytest.mark.parametrize("value",['1,2,3,4,', ',1,2,3', '1,2,,4', '1\n,2', 'nonum', 'test,test', '10,something', 'other,20'])
def test_not_ints(value):
    with pytest.raises(ValueError, match=r"invalid literal for int\(\) with base 10:*"):
        add_string(value)
