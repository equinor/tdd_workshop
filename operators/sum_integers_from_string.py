def sum_integers_from_string(input_string):

    input_string = input_string.replace("\n", ",")

    if (",," in input_string):
        return 0

    if len(input_string) == 1 or len(input_string) % 2 == 0:
        return 0

    splitted_str = input_string.split(",")

    return sum(int(val) for val in splitted_str)