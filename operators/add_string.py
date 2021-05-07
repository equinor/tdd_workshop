def add_string(input):
    if input == "":
        values = [0]
    else:
        values = input.split(",")
        for i, value in enumerate(values):
            values[i] = float(value)
    return sum(values)
