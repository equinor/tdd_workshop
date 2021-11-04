from operators.string_to_number import string_to_int


def add_multiple_numbers_string(input_string):
    input_numbers = map(string_to_int, input_string.split(","))
    return sum(input_numbers)
