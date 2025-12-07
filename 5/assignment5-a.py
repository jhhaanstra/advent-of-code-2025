ranges = []

with open('5/input-ranges') as file:
    for line in file.readlines():
        outers = line.split('-')
        ranges.append(range(int(outers[0]), int(outers[1]) + 1))

fresh_ingredients = set().union(*ranges)

nr_fresh = 0
with open('5/input-values') as file:
    for line in file.readlines():
        if int(line) in fresh_ingredients:
            nr_fresh += 1

print(nr_fresh)