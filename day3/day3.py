"""Day 3: Toboggan Trajectory"""

"""
Part 1
input: 2d array/grid - "." open space, "#" tree
output: number of trees encountered

start: top left corner
pattern going down = 3 to the right and 1 down
end: bottom right corner

input notes - oh my god the input is ONE pattern..
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
    return

print(toboggan_trajectory(example))
