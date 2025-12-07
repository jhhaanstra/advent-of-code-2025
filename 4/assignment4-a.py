def _is_spot_taken(grid: list[list[bool]], x: int, y: int) -> bool:
    try:
        return grid[y][x] == True
    except IndexError:
        return False


def _is_accessible(grid: list[list[bool]], x: int, y: int) -> bool:
    nr_spots_taken = 0

    for curr_y in range(max(y - 1, 0), y + 2):
        for curr_x in range(max(x - 1, 0), x + 2):
            if y == curr_y and x == curr_x:
                continue            
            
            if _is_spot_taken(grid, curr_x, curr_y):
                nr_spots_taken += 1

    return nr_spots_taken < 4

def _scan(grid: list[list[bool]]):
    accessible = []

    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if _is_spot_taken(grid, x, y) and _is_accessible(grid, x, y):
                accessible.append((y, x))

    return accessible

grid = []

with open('4/input') as file:
    for line in file.readlines():
        grid.append(list(map(lambda x : x == '@', line.strip())))


accessible_coords = _scan(grid)
accessible = len(accessible_coords)


while accessible_coords:
    for coord in accessible_coords:
        grid[coord[0]][coord[1]] = False

    accessible_coords = _scan(grid)
    accessible += len(accessible_coords)

for y in grid:
    print(''.join(list(map(lambda x : '@' if x == True else '.', y))))
        
print(accessible)