"""Day 3: Toboggan Trajectory"""

"""
Part 1
input: grid - "." open space, "#" tree; 2d array or just list of strings
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
    pattern = []
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
    while row < height - 1:
        if col < width - 3:
            col += 3
            row += 1
            pos = grid[row][col]
            if pos == '#':
                tree_counter += 1
        else:
            col = col - width
    return tree_counter

# print(toboggan_trajectory(map))

"""
Part 2
input: list of strings
output: int - multiply number of trees for these traversals:
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""
traversals = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def multiplied_trees(grid, traversals_list):
    multiply_trees = 0
    for direction in traversals_list:
        trees = toboggan_trajectories(grid, direction)
        if trees > 0 and multiply_trees == 0:
            multiply_trees = trees
        else:
            multiply_trees *= trees
    return multiply_trees

def toboggan_trajectories(grid, traversal):
    height = len(grid)
    width = len(grid[0])
    row = col = 0
    right, down = traversal
    trees = 0
    while row < height - 1:
        if col < width - right:
            col += right
            row += down
            if grid[row][col] == '#':
                trees += 1
        else:
            col = col - width
    return trees

print(multiplied_trees(map, traversals))
