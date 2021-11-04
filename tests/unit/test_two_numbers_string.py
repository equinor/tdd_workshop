from operators.two_numbers_string import two_numbers_string

def test_two_numbers_string():
    input = "1,2"
    result = two_numbers_string(input)
    assert result == 3