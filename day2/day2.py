"""
Day 2 - Password Philosophy

Notes:
each line gives password policy min_num - max_num letter: password
"""

"""
Part 1
input: list of strings
output: int - number of valid passwords
"""
# opening actual file with passwords
passwords_file = open('input.txt', 'r', encoding='utf-8')
passwords = passwords_file.read().split('\n')
passwords_file.close()

print(passwords)

example = [
'1-3 a: abcde',
'1-3 b: cdefg',
'2-9 c: ccccccccc'
]

def valid_password(passwords):
    return

print(valid_password(example))
