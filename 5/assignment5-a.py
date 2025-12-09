ranges = []

with open('5/input-ranges') as file:
    for line in file.readlines():
        outers = line.split('-')
        ranges.append((int(outers[0]), int(outers[1])))

ranges.sort(key=lambda x: x[0])
ranges.reverse()

nr_fresh = 0
with open('5/input-values') as file:
    for line in file.readlines():
        value = int(line)

        for range in ranges:
            if range[0] <= value:
               if (range[1] >= value):
                    print(value)
                    nr_fresh += 1
                    break

print(nr_fresh)