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

def finding_final(layout):
    return

def seating_system(final_layout):
    return
