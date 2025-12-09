with open('7/input') as file:
    lines = list(map(lambda x : x.strip(), file.readlines()))
    current_beam_positions = set([lines[0].index('S')])
    nr_hits = 0

    for line in lines[1:]:
        hits = list(filter(lambda pos : line[pos] == '^', current_beam_positions))
        for hit in hits:
            nr_hits += 1
            current_beam_positions.remove(hit)
            current_beam_positions.add(hit - 1)
            current_beam_positions.add(hit + 1)

        printer = ''
        for i in range(len(line)):
            if i in hits:
                printer += '^'
            elif i in current_beam_positions:
                printer += '|'
            else:
                printer += '.'
        print(printer)
    print(nr_hits)