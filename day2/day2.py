"""
Day 2 - Password Philosophy

Notes:
each line gives password policy min_num - max_num letter: password
"""
# opening actual file with passwords
passwords_file = open('input.txt', 'r', encoding='utf-8')
passwords_input = passwords_file.read().split('\n')
passwords_file.close()

passwords_input = passwords_input[:len(passwords_input) - 1] #getting rid of last ele = empty string

# print(passwords)

example = [
'1-3 a: abcde',
'1-3 b: cdefg',
'2-9 c: ccccccccc'
]

"""
Part 1
input: list of strings
output: int - number of valid passwords

thoughts:
each line, split on the space = separate policy, letter, and password -> list of lists of strings
"""

def valid_password(passwords):
    # outside function - split password into parts
    separate_parts(passwords)
    # print(passwords)
    # split password and get min and max numbers
    min_max(passwords)
    # get target letter
    target_letter(passwords)
    print(passwords)
    # look at password w/ counter for target letter
    valid = 0
    for password in passwords:
        counter = 0
        condition, letter, check_password = password
        min, max = condition
        for char in check_password:
            if char == letter:
                counter += 1
        if counter >= min and counter <= max:
            valid += 1
        else:
            print('invalid', password)
    return valid

def separate_parts(passwords):
    for idx, password in enumerate(passwords):
        passwords[idx] = password.split(' ')
    return passwords

def min_max(passwords):
    for password in passwords:
        conditions = password[0]
        conditions_split = conditions.split('-')
        min, max = conditions_split
        min = int(min)
        max = int(max)
        password[0] = [min, max]
    return passwords

def target_letter(passwords):
    for password in passwords:
        letter = password[1][:1]
        password[1] = letter
    return passwords

# print(valid_password(example)) #2! the second password is invalid
print(valid_password(passwords_input))
