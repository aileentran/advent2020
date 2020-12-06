import math

"""
Day 5: Binary Boarding

Part 1
input: list of strings - 10 chars
output: num - HIGHEST seat id = row * 8 + col

Notes:
first 7 chars indicate which specific row
last 3 chars indicate which col in row = seat
plane: 128 rows, 8 cols of seats

Example and explanation
BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
"""

def open_file(file_name):
    file = open(file_name, 'r')
    binary = []
    for line in file:
        line = line.rstrip('\n')
        binary.append(line)
    return binary

example = open_file('example.txt')
input = open_file('input.txt')

def binary_boarding(binary):
    highest_id = 0
    for b in binary:
        row_dir = b[:7]
        col_dir = b[7:]
        row = binary_search(row_dir)
        col = binary_search(col_dir)
        seat_id = row * 8 + col
        print('row', row)
        print('col', col)
        print('seat_id', seat_id)
    if seat_id > highest_id:
        highest_id = seat_id
    return highest_id

def binary_search(directions):
    target = 0
    if directions[0] == 'F' or directions[0] == 'B':
        lower, upper = 0, 127
    else:
        lower, upper = 0, 7
    for dir in directions:
        diff = abs(upper - lower)
        if dir == 'F' or dir == 'L':
            upper -= diff // 2
        else:
            lower += diff // 2
    last = directions[-1]
    if last == 'F' or last == 'L':
        target = lower
    else:
        target = upper
    return target

print(binary_boarding(example))
# print(binary_boarding(input))
