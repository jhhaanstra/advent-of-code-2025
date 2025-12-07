#!/usr/bin/python3
from math import floor, ceil

dial = 50
counter = 0

with open('1/test-input') as file:
    for line in file:
        direction = 1 if line[0] == 'R' else -1
        value = int(line[1::])

        counter += value // 100
        value %= 100

        for i in range(value):
            dial = (dial + direction) % 100
            if dial == 0:
                counter += 1

        print(dial)

print(counter)