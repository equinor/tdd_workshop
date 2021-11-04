from operators.string_to_number import string_to_int


def sum_numbers_in_string(string_input):
    first_number, second_number = map(string_to_int, string_input.split(","))
    return first_number + second_number
