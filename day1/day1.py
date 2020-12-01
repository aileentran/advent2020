"""
Day 1: Report Repair

input: list of numbers
output: num - find 2 entries that sum to 2020 and multiply them
"""
# opening file and converting text to ints!
expense = open("day1_input.txt", "r", encoding="utf-8")
expense_str = expense.read().split('\n') #an empty string at end of list
expense.close()

expense_str = expense_str[:len(expense_str) - 1]
expense_nums = []

for string in expense_str:
    num = int(string)
    expense_nums.append(num)

def multiply_sums(nums):
    for num in nums:
        diff = 2020 - num
        if diff in nums:
            return num * diff
    return "Nothing sums to 2020!"

print(multiply_sums(expense_nums))
