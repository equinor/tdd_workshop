from operators.add_multiple_numbers_string import add_multiple_numbers_string


def test_add_multiple_numbers_string():
    input = "1, 2, 3, 4"
    result = add_multiple_numbers_string(input)
    assert result == 10
