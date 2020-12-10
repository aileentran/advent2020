"""
Day 10: Adapter Array

Part 1
input: list of nums - jolts for the adapters
output: num - 1 jolt diff count * 3 jolt diff count
Note - include your device += 3 greatest jolt amount
"""
def open_file(file_name):
    file = open(file_name, 'r')
    adapters = []
    for line in file:
        line = line.rstrip('\n')
        adapters.append(int(line))
    return adapters
example1 = open_file('example1.txt')
example2 = open_file('example2.txt')
input = open_file('input.txt')

def adapter_array(adapters):
    outlet = 0
    adapters.append(outlet)
    adapters.sort()
    device = adapters[-1] + 3
    adapters.append(device)
    diffs = {}
    for i in range(len(adapters) - 1):
        a1 = adapters[i]
        a2 = adapters[i + 1]
        diff = abs(a1 - a2)
        if diff not in diffs.keys():
            diffs[diff] = 0
        diffs[diff] += 1
    return diffs[1] * diffs[3]


# print(adapter_array(example1))
# print(adapter_array(example2))
# print(adapter_array(input))

"""
Part 2
input: list of adapters (including outlet and device)
output: num of ways it can be arranged
"""
def adapter_arrangments(adapters):
    outlet = 0
    adapters.append(outlet)
    adapters.sort()
    device = adapters[-1] + 3
    adapters.append(device)

    arrangements = set(adapters)
    

    return arrangements

print(adapter_arrangments(example1))
# print(adapter_arrangments(example2))
# print(adapter_arrangments(input))
