"""Day 1: Report Repair"""
# opening file and converting text to ints!
expense = open("day1_input.txt", "r", encoding="utf-8")
expense_str = expense.read().split("\n") #an empty string at end of list
expense.close()

expense_str = expense_str[:len(expense_str) - 1]
expense_nums = []

for string in expense_str:
    num = int(string)
    expense_nums.append(num)
"""
Part 1
input: list of numbers
output: num - find 2 entries that sum to 2020 and multiply them
"""
def multiply_sums(nums):
    expense_idx = {}
    for idx, num in enumerate(nums):
        diff = 2020 - num
        if diff in expense_idx.keys():
            return num * diff
        expense_idx[num] = idx
    return "Nothing sums to 2020!"

# print(multiply_sums(expense_nums))
# run time: O(n) bc fast lookup w/ dictionary
# run space: O(n) -> dictionary length at worst is same length as list

"""
Part 2
input: list of numbers
output: num - find 3 entries that sum to 2020 and multiply them
"""

def multiply_three_sums(nums):
    expense_idx = {}
    for idx1 in range(0, len(nums) - 1):
        num1 = nums[idx1]
        for idx2 in range(idx1 + 1, len(nums)):
            num2 = nums[idx2]
            diff = 2020 - num1 - num2
            if diff <= 0:
                continue
            if diff in expense_idx.keys():
                return diff * num1 * num2
            expense_idx[num2] = idx2
        expense_idx[num1] = idx1
    return "There are NOT 3 nums that sum to 2020"

example = [1721, 979, 366, 299, 675, 1456] #979, 366, 675
print(multiply_three_sums(expense_nums))
# print(multiply_three_sums(example))

# run time: n = len(nums), l = len(n - 1) --> O(n * l) ~ O(n^2)
# run space: worse case, O(n)
