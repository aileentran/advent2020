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
            #     print(f'repeat at {i}', len(instructions), instruction)
            #     return accumulator

# print(accumulator_value(example))
# print(accumulator_value(input))

"""
Part 2
exactly 1 instruction is corrupted from jmp <> nop
figure out which one it is
change it to the other one to reach all the way to the end
output: accumulator
"""
def fixing_corruption(instructions):
    # jmp_nop_counter = 0
    i = len(instructions) - 1
    while i >= 0:
        instruction = instructions[i]
        op, arg = instruction
        # if op == 'nop' or op == 'jmp':
        #     print('jmp_nop_counter', jmp_nop_counter, instruction, i)
        #     jmp_nop_counter += 1
        if op == 'nop':
            instructions[i] = ('jmp', arg)
            return instructions
        if op == 'jmp':
            instructions[i] = ('nop', arg)
            return instructions
        i -= 1
# print(fixing_corruption(example))
# print(fixing_corruption(input))

def uncorrupted_accumulator_value(instructions):
    uncorrupted_instructions = fixing_corruption(instructions)
    index_dict = {} #idx: counter. when a counter hits 2, return accumulator
    accumulator = 0
    # print(uncorrupted_instructions)
    i = 0
    while i < len(uncorrupted_instructions):
        instruction = uncorrupted_instructions[i]
        op, arg = instruction
        # print(instruction)
        # if 2 in index_dict.values():
        #     return accumulator
        if i not in index_dict.keys():
            index_dict[i] = 1
        else: #we've hit two!
            return 'LOOPING!'
        if op == 'nop':
            i += 1
        elif op == 'acc':
            accumulator += arg
            i += 1
        elif op == 'jmp':
            # print('prev')
            i += arg
            if i in index_dict.keys():
                print(f'repeat at {i}', instruction, uncorrupted_instructions[i])
                # return accumulator
    return accumulator

# print(uncorrupted_accumulator_value(example))
print(uncorrupted_accumulator_value(input))
