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
            print(i, instruction)
            return accumulator
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
        # print('copy instructions', i, copy_instructions[i])
        if copy_instructions[i][0] == 'nop' and i != copy_instructions[i][1]:
            copy_instructions[i] = ('jmp', copy_instructions[i][1])
        elif copy_instructions[i][0] == 'jmp':
            copy_instructions[i] = ('nop', copy_instructions[i][1])
        elif copy_instructions[i][0] == 'acc':
            i += 1
            continue
        # print('copy!', copy_instructions)
        index_dict = {} #index:counter
        accumulator = 0
        k = 0
        while k < len(copy_instructions):
            copy_instruction = copy_instructions[k]
            op, arg = copy_instruction
            # print('in k loop', op, arg)
            if k not in index_dict.keys():
                index_dict[k] = 1
            else: #we've hit two!
                # print('loop!')
                break
            # print(index_dict)
            if op == 'nop':
                k += 1
            elif op == 'acc':
                accumulator += arg
                k += 1
            elif op == 'jmp':
                k += arg
            # print('accumulator', accumulator)
            # print('end of k', k, op, arg)
            if k == len(copy_instructions): #bc acc and nop k += 1 so.. 1 more than i
                return accumulator
        i += 1


# print(uncorrupted_accumulator_value(example))
print(uncorrupted_accumulator_value(input))
# print(accumulator_value(input))
