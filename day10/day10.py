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
    outlet = 0
    adapters.append(outlet)
    adapters.sort()
    device = adapters[-1] + 3
    adapters.append(device)
    return adapters
example1 = open_file('example1.txt')
example2 = open_file('example2.txt')
input = open_file('input.txt')

def adapter_array(adapters):
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
tribonnaci_sequence = [1, 1, 2, 4, 7, 13, 24, 44, 81, 149]

def tribonnaci(num):
    if num > len(tribonnaci_sequence):
        return f"Can't calculate %{num}"
    return tribonnaci_sequence[num - 1]

def adapter_arrangements(adapters):
    current = multiplier = 1
    for adapter in adapters:
        if adapter + 1 in adapters:
            current += 1
        else:
            multiplier *= tribonnaci(current)
            current = 1
    return multiplier

# print(adapter_arrangements(example1))
# print(adapter_arrangements(example2))
print(adapter_arrangements(input))
