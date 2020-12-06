"""
Day 6: Custom Customs

input: list of list of letters; each list = 1 group. each item = answers a-z
output: sum of count

thoughts:
turn each group into set of answers. count length of sets and sum them
"""

def open_file(file_name):
    file = open(file_name, 'r')
    groups = []
    group = []
    for line in file:
        line = line.rstrip('\n')
        if line == '':
            groups.append(group)
            group = []
        else:
            group.append(line)
    groups.append(group)
    return groups

example = open_file('example.txt')
input = open_file('input.txt')

def custom_customs(groups):
    sum = 0
    for group in groups:
        answers = group_answers(group)
        sum += len(answers)
    return sum

def group_answers(group):
    answers = set()
    for answer in group:
        for char in answer:
            answers.add(char)
    return answers

# print(custom_customs(example))
print(custom_customs(input))
