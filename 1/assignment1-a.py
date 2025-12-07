#!/usr/bin/python3
dial = 50
counter = 0

with open('input') as file:
    for line in file:
        direction = line[0]
        value = int(line[1::]) % 100
        if direction == 'R':
            dial = (dial + value) % 100
        elif direction == 'L':
            dial = ((dial - value) + 100) % 100
        
        if dial == 0:
            counter += 1

print(counter)