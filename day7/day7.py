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
        line = line.rstrip('.')
        rules.append(line)
    return rules
example = open_file('example.txt')
input = open_file('input.txt')
# print(example)

def rules_to_dictionary(rules):
    all_rules = []
    for rule in rules:
        rule = rule.split('contain')
        bag_rule = bag_and_contents(rule)
        all_rules.append(bag_rule)
    return all_rules

def bag_and_contents(rule):
    bag = {}
    outer, contents = rule
    outer = outer.rstrip(' ')
    contents = contents.split(',')
    has_contents = {}
    for content in contents:
        content = content.lstrip(' ')
        info = content.split(' ')
        amount = info[0]
        if amount == 'no':
            bag[outer] = content
            return bag
        else:
            # specifics = {}
            bag_info = ' '.join(info[1:])
            bag_info = bag_info.rstrip('s') #make it easy to search bag later?
            has_contents[bag_info] = int(amount)
    bag[outer] = has_contents
    return bag
# print(rules_to_dictionary(example))

def handy_haversacks(rules):
    dict_rules = rules_to_dictionary(rules)
    bag_colors = 0
    for rule in dict_rules:
        print(rule)
        # print(dict_rules[rule])
        # contents = dict_rules[bag]
        # print('bag', bag, contents)

print(handy_haversacks(example))
