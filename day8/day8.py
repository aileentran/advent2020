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
        if i not in index_dict.keys():
            index_dict[i] = 1
        else: #we've hit two!
            # print(i, instruction)
            return 'loop'
        if op == 'nop':
            i += 1
        elif op == 'acc':
            accumulator += arg
            i += 1
        elif op == 'jmp':
            i += arg
    return accumulator

# print(accumulator_value(example))
# print(accumulator_value(input))

"""
Part 2
exactly 1 instruction is corrupted from jmp <> nop
figure out which one it is
change it to the other one to reach all the way to the end
output: accumulator
Note:
same instruction can appear again at diff idxs
"""

def uncorrupted_accumulator_value(instructions):
    i = 0
    while i < len(instructions):
        copy_instructions = instructions.copy()
        if copy_instructions[i][0] == 'nop' and i != copy_instructions[i][1]:
            copy_instructions[i] = ('jmp', copy_instructions[i][1])
        elif copy_instructions[i][0] == 'jmp':
            copy_instructions[i] = ('nop', copy_instructions[i][1])
        elif copy_instructions[i][0] == 'acc':
            i += 1
            continue
        accumulator = accumulator_value(copy_instructions)
        if accumulator != 'loop':
            return accumulator
        i += 1


print(uncorrupted_accumulator_value(example))
# print(uncorrupted_accumulator_value(input))
# print(accumulator_value(input))
