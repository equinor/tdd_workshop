def add_string(input):
    values = input.split(",")
    for i, value in enumerate(values):
        values[i] = float(value)
    return sum(values)
