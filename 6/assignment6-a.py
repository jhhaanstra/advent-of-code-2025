from functools import reduce

grid = []
results = []
with open('6/input') as file:
    lines = file.readlines()
    for line in lines[:-1]:
        nrs = list(filter(lambda x : len(x) != 0, map(lambda x: x.strip(), line.split(' '))))
        grid.append(nrs)


    operators = list(filter(lambda x : len(x) != 0, map(lambda x: x.strip(), lines[-1].split(' '))))
    for i in range(len(operators)):
        operator = operators[i]
        operation = lambda x : x

        if operator == '*':
            operation = lambda x, y: x * y
        else:
            operation = lambda x, y: x + y

        results.append(reduce(operation, map(lambda x : int(x[i]), grid)))

    print(sum(results))
    