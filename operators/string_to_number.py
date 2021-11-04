def string_to_int(string_input):

    if not string_input:
        raise ValueError("Converting string to integer failed")

    if "," in string_input:
        numbers = string_input.split(",")
        int_output = sum([int(x) for x in numbers])
    else:
        int_output = int(string_input)

    return int_output
