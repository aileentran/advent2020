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
