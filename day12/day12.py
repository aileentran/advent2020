"""
Day 12 - Rain Risk

Part 1
input: navigation instructions - list of strings "letter#"
output: num - distance between location and Manhattan starting position

Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.

Manhattan distance (sum of the absolute values of its east/west position and its north/south position)

Ship starts facing East!
"""
def open_file(file_name):
    file = open(file_name, 'r')
    instructions = []
    for line in file:
        line = line.rstrip('\n')
        dir = line[0:1]
        val = int(line[1:])
        instructions.append((dir, val))
    return instructions
example = open_file('example.txt')
input = open_file('input.txt')
# print(example)
# print(input)

def distance(instructions, starting_dir):
    compass = ['N', 'E', 'S', 'W'] #right: idx + 1 % 4?, left: -1
    start = starting_dir
    east_west = 0
    north_south = 0
    for ins in instructions:
        dir, val = ins
        compass_idx = compass.index(start)
        turn = val // 90
        if dir == 'R':
            start = compass[(compass_idx + turn) % 4]
            dir = start
            continue
        if dir == 'L':
            start = compass[compass_idx - turn]
            dir = start
            continue

        if dir == 'F':
            dir = start
        if dir == 'N':
            north_south += val
        elif dir == 'S':
            north_south -= val
        elif dir == 'E':
            east_west += val
        elif dir == 'W':
            east_west -= val
    return abs(east_west) + abs(north_south)
# print(distance(example, 'E'))
# print(distance(input, 'E'))
