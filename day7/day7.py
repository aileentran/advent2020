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
example1 = open_file('example1.txt')
example2 = open_file('example2.txt')
input = open_file('input.txt')

def rules_to_dictionary(rules):
    all_rules = {}
    for rule in rules:
        rule = rule.split('contain')
        bag_rule = bag_and_contents(rule)
        # print('bag_rule', bag_rule)
        all_rules.update(bag_rule)
    return all_rules

def bag_and_contents(rule):
    bag = {}
    outer, contents = rule
    outer = outer.rstrip(' ')
    outer = outer.rstrip('s')
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
            bag_info = ' '.join(info[1:])
            bag_info = bag_info.rstrip('s') #make it easy to search bag later?
            has_contents[bag_info] = int(amount)
    bag[outer] = has_contents
    return bag
print(rules_to_dictionary(example2))
print(rules_to_dictionary(example1))
"""Part 1"""
def handy_haversacks(rules):
    dict_rules = rules_to_dictionary(rules)
    holds_shiny = directly_holds_shiny(dict_rules)
    bags = indirectly_holds(dict_rules, holds_shiny)
    old_bag_count = len(holds_shiny)
    curr_bag_count = len(bags)
    # have a counter to keep track of previous loop of bags
    # if once counter == loops amount, break out of it and return num of bags
    while old_bag_count < curr_bag_count:
        all_bags = indirectly_holds(dict_rules, bags)
        bags = all_bags
        old_bag_count = curr_bag_count
        curr_bag_count = len(all_bags)
    return curr_bag_count

def directly_holds_shiny(rules):
    holds_shiny = set()
    for rule in rules:
        for bag in rule:
            contents = rule[bag]
            if contents == 'no other bags':
                continue
            contents = contents.keys()
            if 'shiny gold bag' in contents:
                holds_shiny.add(bag)
    return holds_shiny

def indirectly_holds(rules, holds_shiny):
    all_bags = set()
    all_bags.update(holds_shiny)
    for rule in rules:
      for bag in rule:
          contents = rule[bag]
          if contents == 'no other bags':
              continue
          else:
              contents = contents.keys()
          for content in contents:
              if content in all_bags:
                  all_bags.add(bag)
    return all_bags

# print(handy_haversacks(example1)) #6
# print(handy_haversacks(input)) #332

"""
Part 2 - how many bags does the shiny bag hold??
add bags that shiny holds
example1 = 32 bags
example2 = 126 bags
"""

def shiny_hold(rules):
    bags = rules_to_dictionary(rules)
    # print(bags)
    # wait wait.. maybe change input to one gigantic ditionary of rules?

print(shiny_hold(example1))
# print(shiny_hold(example2))
# print(shiny_hold(input))
