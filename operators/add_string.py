def add_string(input_string):
    if input_string == '':
        return 0
    return sum(map(complex, input_string.split(",")))
