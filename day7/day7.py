"""
Day 7: Handy Haversacks

input: list of rules - convert into dictionary w/ counter??
output: num - how many bags can carry at least one shiny gold bag?
"""
def open_file(file_name):
    file = open(file_name, 'r')
    rules = []
    for line in file:
        line = line.rstrip('\n')
        rules.append(line)
    return rules
example = open_file('example.txt')
input = open_file('input.txt')
print(example)
