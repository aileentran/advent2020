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

"""
Part 2
input: list of instructions (letter, units)
output: Manhattan distance btwn starting and current location

Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.
Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
Action F means to move forward to the waypoint a number of times equal to the given value.

waypoint 10 east, 1 north relative to the ship

only time ship moves w/ F

adjust waypoint until F
then multiply waypoint by F = current location
"""

def relative_waypoint(instructions, waypoint):
    east_west = 0
    north_south = 0

    for ins in instructions:
        dir, val = ins
        print('ins', ins)
        if dir == 'F': #moving ship towards waypoint
            for coord in waypoint:
                if coord[0] == 'E':
                    east_west += coord[1] * val
                elif coord[0] == 'W':
                    east_west -= coord[1] * val
                elif coord[0] == 'N':
                    north_south += coord[1] * val
                elif coord[0] == 'S':
                    north_south -= coord[1] * val
            print(east_west, north_south)
        elif dir == 'L' or dir == 'R': #changing waypoint direction
            waypoint = change_direction(waypoint, ins)
            # print(waypoint)
        else:
            waypoint = change_distance(waypoint, ins)
            # print(waypoint)
    return abs(east_west) + abs(north_south)

def change_direction(waypoint, ins):
    coord1, coord2 = waypoint
    dir, val = ins
    compass = ['N', 'E', 'S', 'W']
    coord1_idx = compass.index(coord1[0])
    coord2_idx = compass.index(coord2[0])
    turn = val // 90
    if dir == 'L':
        coord1[0] = compass[coord1_idx - turn]
        coord2[0] = compass[coord2_idx - turn]
    if dir == 'R':
        coord1[0] = compass[(coord1_idx + turn) % 4]
        coord2[0] = compass[(coord2_idx + turn) % 4]
    waypoint = [coord1, coord2]
    return waypoint

def change_distance(waypoint, ins):
    dir, val = ins
    for coord in waypoint:
        if coord[0] == dir:
            coord[1] += val
    return waypoint


waypoint = [['E', 10], ['N', 1]]
# print(relative_waypoint(example, waypoint))
print(relative_waypoint(input, waypoint))
