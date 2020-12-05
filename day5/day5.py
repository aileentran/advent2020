"""
Day 5: Binary Boarding

Part 1
input: list of strings - 10 chars
output: num - seat id = row * 8 + col

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
    return

print(binary_boarding(example))
# print(binary_boarding(input))
