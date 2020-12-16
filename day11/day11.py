"""
Day 11: Seating System

Part 1
input: 2d array of strings
output: num - how many seats are occupied?

Rules
If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.

Repeat rules until seats no longer change
"""
import copy

def open_file(file_name):
    file = open(file_name, 'r')
    layout = []
    for line in file:
        line = line.rstrip('\n')
        layout.append(list(line))
    return layout

example = open_file('example.txt')
input = open_file('input.txt')

def valid_adjacent(curr, width, height):
    r_idx, c_idx = curr
    potential_adj = [(r_idx - 1, c_idx - 1), (r_idx - 1, c_idx), (r_idx - 1, c_idx + 1),
    (r_idx, c_idx - 1), (r_idx, c_idx + 1),
    (r_idx + 1, c_idx - 1), (r_idx + 1, c_idx), (r_idx + 1, c_idx + 1)]
    adj = []
    for potential in potential_adj:
        r, c = potential
        if r >= 0 and c >= 0 and r < height and c < width:
            adj.append(potential)
    return adj

def finding_final(layout):
    current = layout.copy()
    next = layout.copy()
    width = len(layout[0])
    height = len(layout)
    final = current

    for r_idx, row in enumerate(current):
        for c_idx, col in enumerate(row):
            adj = valid_adjacent((r_idx, c_idx), width, height)
            occupied = 0
            # print('curr', current[r_idx][c_idx])
            for a_idx, a in enumerate(adj):
                r_adj, c_adj = a
                seat = current[r_adj][c_adj]
                if seat == '#':
                    occupied += 1
                # if seat == '.': #removing floor
                #     adj.pop(a_idx)

            if current[r_idx][c_idx] == 'L' and occupied == 0:
                next[r_idx][c_idx] = '#'
            if current[r_idx][c_idx] == '#' and occupied >= len(adj) / 2:
                next[r_idx][c_idx] = 'L'
    #currently directly manipulating layout.
    #TODO: create copy so not to interfere with L and # assignment
    #TODO: figure out occupied for < 4 adjacent seats i.e. edges and things
    print('current', current)
    print('next', next)
    print(layout)


    return

print(finding_final(example))

def seating_system(final_layout):
    return
