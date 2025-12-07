numbers = []

def _find_jolt(nrs: list[int], length: int, current: list[int]) -> int:
    max_value = 0
    max_index = 0

    to_add = length - len(current)
    scan_size = len(nrs) - (to_add - 1)
    
    for i in range(scan_size):
        if nrs[i] > max_value:
            max_value = nrs[i]
            max_index = i
    
    current.append(max_value)

    if len(current) == length:
        return int("".join(map(str, current)))
    else:
        return _find_jolt(nrs[max_index + 1::], length, current)

with open("3/input") as file:
    for line in list(map(lambda x: x.strip(), file.readlines())):
        print(line)
        value = _find_jolt(list(map(lambda x: int(x), line)), 12, [])
        print("jolt: {}".format(value))
        numbers.append(value)

print(sum(numbers))