"""
Day 9: Encoding Error

Part 1
input: list of numbers
output: num - the first number that does not follow rules

input.txt rules:
25 number preamble that moves down the list
26th num = sum of any 2 nums in preamble

example.txt rules:
5 number preamble that moves down the list
6th number = sum of any 2 nums in the preamble
"""
def open_file(file_name):
    file = open(file_name, 'r')
    nums = []
    for line in file:
        line = int(line.rstrip('\n'))
        nums.append(line)
    return nums
example = open_file('example.txt')
input = open_file('input.txt')

def encoding_error(nums, preamble):
    i = 0
    while i < len(nums) - preamble:
        preamble_nums = nums[i:i + preamble]
        sum_num = nums[i + preamble]
        for p_idx, num in enumerate(preamble_nums):
            diff = sum_num - num
            if p_idx == len(preamble_nums) - 1 and diff not in preamble_nums:
                return sum_num
            if diff in preamble_nums:
                break
        i += 1

# print(encoding_error(example, 5))
# print(encoding_error(input, 25))

"""
Part 2
find contiguous set of 2+ nums that sum to nonencrypted from part 1
input: list of numbers
output: num - sum smallest and largest in contiguous range
"""
def encryption_weakness(nums, preamble):
    error = encoding_error(nums, preamble)
    for i in range(len(nums) - preamble):
        sum_error = []
        for k in range(i, i + preamble):
            summing_list = sum(sum_error)
            if summing_list != error:
                sum_error.append(nums[k])
            else:
                return min(sum_error) + max(sum_error)

# print(encryption_weakness(example, 5))
print(encryption_weakness(input, 25))
