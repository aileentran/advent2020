"""Day 3: Toboggan Trajectory"""

"""
Part 1
input: 2d array/grid - "." open space, "#" tree
output: number of trees encountered

start: top left corner
pattern going down = 3 to the right and 1 down
end: bottom right corner

input notes - oh my god the input is ONE pattern..

how many patterns do we need?
3 right, 1 down
orrr loop through the same pattern and keep track of where to start next
grid[row][col]
row = grid idx
col = string idx
"""
def open_file(file_name):
    pattern = list()
    file = open(file_name, "r")
    for line in file:
        # remove newline character
        line = line.rstrip('\n')
        pattern.append(line)
    file.close()
    return pattern
map = open_file('input.txt')
example = open_file('example.txt')

def toboggan_trajectory(grid):
    height = len(grid)
    width = len(grid[0])
    row = col = 0
    tree_counter = 0
    # the end is where row_idx = height - 1
    print('height', height)
    print('width', width)
    while row < height - 1:
        if col < width - 3:
            col += 3
            row += 1
            # print(grid[row])
            # print('row', row)
            # print('col', col)

            pos = grid[row][col]
            if pos == '#':
                # print('TREE!')
                tree_counter += 1

            # print('POSITION', pos)
            # print('\n')
        else:
            # print('You have reached the edge!')
            col = col - width
    return tree_counter

print(toboggan_trajectory(map))
