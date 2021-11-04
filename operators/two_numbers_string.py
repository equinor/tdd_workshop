from operators.string_to_number import string_to_int

def two_numbers_string(string_input):
    number_strings = string_input.split(',')
    number_integers = list(map(string_to_int, number_strings))
    return number_integers[0] + number_integers[1]