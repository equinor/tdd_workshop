from operators.add_string import add_two_numbers_from_string

def test_add_two_numbers_from_string():
    input_string = "1,2"
    expected_result = 3
    result = add_two_numbers_from_string(input_string)
    assert result == expected_result
