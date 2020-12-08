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
# print(rules_to_dictionary(example))

def handy_haversacks(rules):
    dict_rules = rules_to_dictionary(rules)
    holds_target = set()
    seen = 0
    colors = 0
    holds_shiny = directly_holds_shiny(rules)
    print('directly has shiny', holds_shiny)
    # print(len(holds_target))
    # count bags that hold bags that hold shiny gold bag
    # 4 of loops below to reach answer..
    for rule in dict_rules:
      # print('rule', rule)
      for bag in rule:
          # print(rule[bag])
          contents = rule[bag]
          if contents == 'no other bags':
              continue
          else:
              contents = contents.keys()
          for content in contents:
              if content in holds_target:
                  holds_target.add(bag)
    # print(holds_target)
    # print(len(holds_target))
    return len(holds_target)

def directly_holds_shiny(rules):
    dict_rules = rules_to_dictionary(rules)
    holds_shiny = set()
    for rule in dict_rules:
        for bag in rule:
            contents = rule[bag]
            if contents == 'no other bags':
                continue
            contents = contents.keys()
            if 'shiny gold bag' in contents:
                holds_shiny.add(bag)
    return holds_shiny


# somehow check for bags that hold bags that hold shiny gold bag? degrees removed!
# seems to be able to catch degrees removed from shiny gold bag
print(handy_haversacks(example))
# print(handy_haversacks(input))
