"""Day 3: Toboggan Trajectory"""

"""
Part 1
input: 2d array/grid - "." open space, "#" tree
output: number of trees encountered

start: top left corner
pattern going down = 3 to the right and 1 down
end: bottom right corner

input notes - errm.. maybe keep track of the slopes
once the whole thing repeats, it's the set/pattern?
OR PUT IT INTO A SET?!?!?! get a unique pattern! somehow..
OR just find idxs where the first row is repeated??
then slice it to see if it's a repeated pattern?
then we know how to count to the "right"
"""
# Actual input
map_file = open('input.txt', 'r', encoding='utf-8')
map_input = map_file.read().split('\n')
map_file.close()

map_input = map_input[:len(map_input) - 1]
map = []
for slope in map_input:
    map.append([slope])

# print(map)

# Example input - 7 trees
example_file = open('example.txt', 'r', encoding='utf-8')
example_input = example_file.read().split('\n')
example_file.close()

example_input = example_input[:len(example_input) - 1]
example = []
for slope in example_input:
    example.append([slope])

# print(example)
def toboggan_trajectory(grid):
    repeat = 1
    first = grid[0]
    repeat_grid = set(grid)

    # for row in range(1, len(grid)):
    #     slope = grid[row]
    #     if slope == first:
    #         repeat += 1
    #     elif repeat == 1:
    #         repeat_grid.append(slope)

    # print('repeat count', repeat)
    # print('first', first)
    print('repeat grid', repeat_grid)
    # print('length of grid', len(grid))
    # print('length of repeat', len(repeat_grid))
    return

print(toboggan_trajectory(example))
