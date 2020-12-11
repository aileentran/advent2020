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
    # outlet = 0
    # adapters.append(outlet)
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
"""
# adapter_arrangments([0], input_text)
def adapter_arrangements2(left, right):
    count = 0
    appendings = []

    if left[-1] + 3 == highest+3var
        return 1
    end

    right.each do |a|
        if left.last + 3 <= a
            appendings.append(a)
        end
    end

    appendings.each do |a|
        count += adapter_arrangements2(left + a, next_right.pluck(a))
    end

    return count
"""

def adapter_arrangements(left, right, device):
    left_copy = left.copy()
    right_copy = right.copy()
    count = 0
    appendings = []
    print(left)
    if left_copy[-1] == device:
        # print('base case', left_copy)
        # print('leftmost num', left_copy[-1])
        # print('base case device', device)
        # print(left_copy[-1] == device)
        return 1

    for adapter in right_copy:
        # print(left_copy[-1], adapter)
        if abs(left_copy[-1] - adapter) <= 3:
            appendings.append(adapter)
    # print('appendings', appendings)
    for appending in appendings:
        # print('appending', appending, appendings)
        # print('left', left_copy, len(left_copy))
        # print('right', right_copy)
        right_copy.remove(appending)
        left_copy.append(appending)
        count += adapter_arrangements(left_copy, right_copy, device)

    return count

# print(adapter_arrangements([0], example1, example1[-1]))
# print(adapter_arrangements([0], example2, example2[-1]))
print(adapter_arrangements([0], input, input[-1]))
