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
# print(custom_customs(input))

"""
Part 2
identify when EVERYONE in the GROUP answers yes!

thoughts:
get length of the group
make a dictionary counter of answers
loop through dictionary and sum answers that hit the num of peeps in group
"""

def all_yes(groups):
    sum = 0
    for group in groups:
        same = same_answers(group)
        sum += same
    return sum

def same_answers(group):
    group_num = len(group)
    all_answers = {}
    same = 0
    for answers in group:
        for answer in answers:
            if answer not in all_answers.keys():
                all_answers[answer] = 0
            all_answers[answer] += 1
    for response in all_answers:
        if all_answers[response] == group_num:
            same += 1
    return same

# print(all_yes(example))
print(all_yes(input))
