from math import sqrt
import textwrap

def _is_repeating(input: int) -> bool:
    str_input = str(input)
    input_length = len(str_input)

    divisors = []

    for i in range(1, int(sqrt(input_length)) + 1):
        if input_length % i == 0:
            divisors.append(i)
            if i != input_length // i:
                divisors.append(input_length // i)

    divisors.remove(input_length)

    for divisor in divisors:
        wrapped = textwrap.wrap(str_input, divisor)
        if all(x == wrapped[0] for x in wrapped):
            return True
        
    return False


def _calculate_invalid_ids(input: tuple[int, int]) -> int:
    test = list(filter(_is_repeating, range(input[0], input[1] + 1)))
    test_sum = sum(test)
    return test_sum


file = open('2/test-input', 'r')
input = file.readline()
ranges = list(map(lambda r: tuple(map(int, r.split('-'))), input.split(',')))
print(ranges)
print(sum([_calculate_invalid_ids(range) for range in ranges]))
