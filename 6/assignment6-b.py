from functools import reduce

grid = []
results = []
with open('6/input') as file:
    lines = file.readlines()

    number_lines = lines[0:4]
    current_row = []
    for c in range(len(number_lines[0])):
        number_string = ''
        for i in range(0, 4):
            number_string += number_lines[i][c]
        
        number_string = number_string.strip()
        if len(number_string) == 0:
            grid.append(current_row)
            current_row = []
        else:
            current_row.append(int(number_string))

    operators = list(filter(lambda x : len(x) != 0, map(lambda x: x.strip(), lines[4].split(' '))))

for i in range(len(operators)):
    operator = operators[i]
    operation = (lambda x, y: x * y)if operator == '*' else (lambda x, y: x + y)
    results.append(reduce(operation, grid[i]))

print(sum(results))
