
def _ranges_overlap(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return len(range(max(a[0], b[0]), min(a[1], b[1]))) is not 0 or a[1] == b[0]

def _combine(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    new_ranges = [ranges[0]]

    for r in ranges[1:]:
        added = False

        for nr in new_ranges:
            if _ranges_overlap(r, nr):
                new_ranges.remove(nr)
                new_ranges.append((
                    min(r[0], nr[0]), 
                    max(r[1], nr[1])
                ))
                added = True
                break

        if not added:
            new_ranges.append(r)
    
    return new_ranges


ranges = []

with open('5/input-ranges') as file:
    for line in file.readlines():
        outers = line.split('-')
        ranges.append((int(outers[0]), int(outers[1])))

ranges.sort(key=lambda x: x[0])


r1 = _combine(ranges)
r2 = ranges

while r1 != r2:
    r2 = r1
    r1 = _combine(r1)

total_fresh = 0
for r in r1:
    print(r)
    total_fresh += r[1] - r[0] + 1

print(total_fresh)