import textwrap

def _is_repeating(input: int) -> bool:
    str_input = str(input)
    if len(str_input) % 2 != 0:
        return False
    
    len_input = int(len(str_input) / 2)
    
    return str_input[0:len_input] == str_input[len_input:len(str_input)]

def _calculate_invalid_ids(input: tuple[int, int]) -> list[int]:
    return list(filter(_is_repeating, range(input[0], input[1] + 1)))


file = open('2/input', 'r')
input = file.readline()
ranges = list(map(lambda r: tuple(map(int, r.split('-'))), input.split(',')))
print(sum([sum(_calculate_invalid_ids(range)) for range in ranges]))