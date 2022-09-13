from operators.add_string import add, addSupportsSingleValue


def test_two_numbers_are_equal():
    assert 1 == 1


def test_string_to_int_added():
    assert add("1,2") == 3


def test_single_value_string():
    assert addSupportsSingleValue("1") == 1
    assert add("1,2") == 3


# def test_empty_value_in_string():
#     assert addSupportsSingleValue(",1") == 1
#     assert add("1,2") == 3
