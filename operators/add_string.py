import re
from operators.string_to_number import string_to_int


def add_string(inp):
    if inp == "":
        return 0
    inputs = re.split(",|\n", inp)
    if "" in inputs:
        raise ValueError("Illegal input 😡")
    return sum(map(string_to_int, inputs))
