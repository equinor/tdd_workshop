from re import X
from operators.string_to_number import string_to_int

def add(stringWithNumbers):
    splitted = stringWithNumbers.split(",")
    return string_to_int(splitted[0] + splitted[1]) 