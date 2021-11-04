from operators.sum_integers_from_string import sum_integers_from_string

def test_sum_integers_from_string():
    string_input = "2,3"
    result = sum_integers_from_string(string_input)  
    assert result == 5

def test_sum_integers_from_string_with_only_one_number_should_return_0():
    string_input = "2"
    result = sum_integers_from_string(string_input)
    assert result == 0

def test_sum_integers_from_string_with_invalid_string_should_return_0():
    string_input = "2,"
    result = sum_integers_from_string(string_input)
    assert result == 0

def test_sum_integers_from_string_empty_string_should_return_0():
    string_input = ""
    result = sum_integers_from_string(string_input)
    assert result == 0

def test_valid_sum_function_should_return_6():
    string_input = "1\n2,3"
    result = sum_integers_from_string(string_input)
    assert result == 6

def test_sum_function_should_return_0():
    string_input = "1,\n"
    result = sum_integers_from_string(string_input)
    assert result == 0