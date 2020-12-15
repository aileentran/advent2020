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
    copy = layout.copy()
    width = len(copy[0])
    height = len(copy)
    final = copy

    for r_idx, row in enumerate(copy):
        for c_idx, col in enumerate(row):
            curr = (r_idx, c_idx)
            adj = valid_adjacent(curr, width, height)
            print('curr', curr, copy[r_idx][c_idx])
            for a in adj:
                r_adj, c_adj = a
                seat = copy[r_adj][c_adj]
                print(a, seat)


    return

print(finding_final(example))

def seating_system(final_layout):
    return
