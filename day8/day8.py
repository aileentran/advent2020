"""
Day 8: Handheld Halting
There is an infinite loop
What value is the accumulator before second loop?
input: maybe list of tuples? (action, value)
output: num - accumulator
"""
def open_file(file_name):
    file = open(file_name, 'r')
    instructions = []
    for line in file:
        line = line.rstrip('\n')
        line = line.split(' ')
        instruction_str, num_str = line
        num = int(num_str)
        instructions.append((instruction_str, num))
    return instructions
example = open_file('example.txt')
input = open_file('input.txt')

def accumulator_value(instructions):
    index_dict = {} #idx: counter. when a counter hits 2, return accumulator
    accumulator = 0

    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        op, arg = instruction
        # if 2 in index_dict.values():
        #     return accumulator
        if i not in index_dict.keys():
            index_dict[i] = 1
        else: #we've hit two!
            return accumulator
        if op == 'nop':
            i += 1
        elif op == 'acc':
            accumulator += arg
            i += 1
        elif op == 'jmp':
            i += arg
            # if i in index_dict.keys():
            #     return accumulator

print(accumulator_value(example))
print(accumulator_value(input))
