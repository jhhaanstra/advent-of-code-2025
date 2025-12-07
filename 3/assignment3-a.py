numbers = []

with open("3/test-input") as file:
    for line in list(map(lambda x: x.strip(), file.readlines())):
        print(line)

        max_value_1 = 0
        max_value_1_index = 0
        max_value_2 = 0

        for i in range(0, len(line) - 1):
            if int(line[i]) > max_value_1:
                max_value_1_index = i
                max_value_1 = int(line[i])

        for i in range(max_value_1_index + 1, len(line)):
            if int(line[i]) > max_value_2:
                max_value_2 = int(line[i])

        value = int("{}{}".format(max_value_1, max_value_2))
        print("jolt: {}".format(value))
        numbers.append(value)

print(sum(numbers)) 