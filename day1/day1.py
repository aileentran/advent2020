"""Day 1: Report Repair"""
# opening file and converting text to ints!
expense = open("day1_input.txt", "r", encoding="utf-8")
expense_str = expense.read().split('\n') #an empty string at end of list
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

print(multiply_sums(expense_nums))

"""
Part 2
input: list of numbers
output: num - find 3 entries that sum to 2020 and multiply them
"""

def multiply_three_sums(nums):
    nums.sort()
    print(nums)

# print(multiply_three_sums(expense_nums))
