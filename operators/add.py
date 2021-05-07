# 2
# def add_string(string):
#     return 1 + 2

# 3
# def add_string(string):
#     value_1 = 1
#     value_2 = 2
#     return value_1 + value_2

# 4
# def add_string(string):
#     string_list = string.split(",")
#     value_1 = float(string_list[0])
#     value_2 = float(string_list[1])
#     return value_1 + value_2

# 5
# def add_string(string):
#     string_list = string.split(",")
#     value_list = [float(value) for value in string_list]
#     return value_list[0] + value_list[1]

# 6, 7
# def add_string(string):
#     string_list = string.split(",")
#     value_list = [float(value) for value in string_list]
#     return sum(value_list)

# 8
# def add_string(string):
#     if string == "":
#         string = "0,0"
#     string_list = string.split(",")
#     value_list = [float(value) for value in string_list]
#     return sum(value_list)

# 9, 10, 11
# def add_string(string):
#     if string == "":
#         string = "0,0"
#     string_list = string.split(",")
#     value_list = [float(value) for value in string_list]
#     return sum(value_list)

# 12
# def add_string(string):
#     if string == "":
#         string = "0,0"
#     elif "\n" in string:
#         string = string.replace("\n", ",")

#     string_list = string.split(",")
#     value_list = [float(value) for value in string_list]

#     return sum(value_list)

# 13
# def add_string(string):
#     string_list = string_to_string_list(string)
#     value_list = [float(value) for value in string_list]

#     return sum(value_list)

# def string_to_string_list(string):
#     string_fixed = fix_string(string)
#     string_list = string_fixed.split(",")

#     return string_list

# def fix_string(string):
#     if string == "":
#         string_fixed = "0,0"
#     elif "\n" in string:
#         string_fixed = string.replace("\n", ",")
#     else:
#         string_fixed = string

#     return string_fixed
# refactor
# dicussion: breaking functions
# - one function, one action
# - readability: no need to comment if variables and functions describe what is happening
#

# 14
# def add_string(string):
#     string_list = string_to_string_list(string)
#     value_list = [float(value) for value in string_list]

#     return sum(value_list)

# def string_to_string_list(string):
#     if string[0:2] == "//":
#         delimiter = string[2] # ; for first test
#         string = string[4:] # "1;2"
#     else:
#         delimiter = ","
#     string_fixed = fix_string(string, delimiter)
#     string_list = string_fixed.split(delimiter)

#     return string_list

# def fix_string(string, delimiter):
#     if string == "":
#         string_fixed = "0,0"
#     elif "\n" in string:
#         string_fixed = string.replace("\n", delimiter)
#     else:
#         string_fixed = string

#     return string_fixed


# 15


def add_string(string):
    string_list = string_to_string_list(string)
    value_list = [float(value) for value in string_list]

    return sum(value_list)


def string_to_string_list(string):
    string_with_values, delimiter = check_delimiter(string)
    string_fixed = fix_string(string_with_values, delimiter)
    string_list = string_fixed.split(delimiter)

    return string_list


def check_delimiter(string):
    if string[0:2] == "//":
        delimiter = string[2]  # ; for first test
        string_with_values = string[4:]  # "1;2"
    else:
        delimiter = ","
        string_with_values = string

    return string_with_values, delimiter


def fix_string(string, delimiter):
    if string == "":
        string_fixed = "0,0"
    elif "\n" in string:
        string_fixed = string.replace("\n", delimiter)
    else:
        string_fixed = string

    return string_fixed
