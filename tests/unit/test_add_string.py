from operators.add_string import add_string

# def test_two_numbers_are_equal():
#     assert 1 == 1

# List of tests:

# Test more than 1 number
def test_two_numbers():
    input = "1,2"
    result = add_string(input)
    expected_result = 1 + 2
    assert expected_result == result


# Test 1 number
def test_one_numbers():
    input = "1"
    result = add_string(input)
    expected_result = 1
    assert expected_result == result


# Test input is empty
def test_empty_string():
    input = ""
    result = add_string(input)
    expected_result = 0
    assert expected_result == result
