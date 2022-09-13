from operators.sum_numbers_in_string import sum_numbers_in_string


def test_sum_numbers_in_string():
    assert sum_numbers_in_string("1,2") == 3
    assert sum_numbers_in_string("3,5") == 8
    assert sum_numbers_in_string("10 , 6") == 16
    assert sum_numbers_in_string("1,2,3") == 6
