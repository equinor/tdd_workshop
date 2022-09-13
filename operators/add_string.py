from operators.string_to_number import string_to_int

def add_string(numbers):
    if len(numbers) == 0:
        return 0
    nums = numbers.replace('\n',',').split(',')
    ints = [string_to_int(num) for num in nums]
    return sum(ints)
