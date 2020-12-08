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
            print(instruction)
            return accumulator
        if op == 'nop':
            i += 1
        elif op == 'acc':
            accumulator += arg
            i += 1
        elif op == 'jmp':
            i += arg

# print(accumulator_value(example))
# print(accumulator_value(input))

"""
Part 2
exactly 1 instruction is corrupted from jmp <> nop
figure out which one it is
change it to the other one to reach all the way to the end
output: accumulator
"""
# attempting to fix entire data set
# def fixing_corruption(instructions):
#     # jmp_nop_counter = 0
#     i = len(instructions) - 1
#     while i >= 0:
#         instruction = instructions[i]
#         op, arg = instruction
#         if op == 'nop' or op == 'jmp':
#             print(f'change at {i} idx', instruction)
#         if op == 'nop':
#             instructions[i] = ('jmp', arg)
#             return instructions
#         if op == 'jmp':
#             instructions[i] = ('nop', arg)
#             return instructions
#         i -= 1

# fixing specific line of instruction
def fixing_corruption(instruction):
    op, arg = instruction
    if op == 'nop':
        instruction = ('jmp', arg)
        return instruction
    if op == 'jmp':
        instruction = ('nop', arg)
        return instruction

# print(fixing_corruption(example))
# print(fixing_corruption(input))

def uncorrupted_accumulator_value(instructions):
    index_dict = {} #idx: counter. when a counter hits 2, return accumulator
    accumulator = 0
    op = arg = None

    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        op, arg = instruction
        if i not in index_dict.keys():
            index_dict[i] = 1
        else: #we've hit two!
            print(i, instruction)
            return 'LOOPING'
        if op == 'nop':
            next = i
            next += 1
        elif op == 'acc':
            accumulator += arg
            i += 1
        elif op == 'jmp':
            next = i
            next += arg

        # if next in index_dict.keys():
        #     new_instructions = fixing_corruption(instruction)
        #     print('old', instruction)
        #     print('new', new_instructions)
        #     instructions[next] = new_instructions
        #     print(instructions)
        # else:
        #     i = next
    return accumulator


print(uncorrupted_accumulator_value(example))
# print(uncorrupted_accumulator_value(input))
# print(accumulator_value(input))
