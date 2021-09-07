def sum_two_numbers(numbers: str):
    number_list = [int(n) for n in numbers.split(",")]
    the_sum = sum(number_list)
    return the_sum
