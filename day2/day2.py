"""
Day 2 - Password Philosophy

Notes:
each line gives password policy min_num - max_num letter: password
"""
def open_file(file_name):
    file = open(file_name, 'r')
    password = []
    for line in file:
        line = line.rstrip('\n')
        password.append(line)
    file.close()
    return password
passwords_input = open_file('input.txt')

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
    # split password and get min and max numbers
    min_max(passwords)
    # get target letter
    target_letter(passwords)
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
# print(valid_password(passwords_input))


"""
Part 2
condition actually describes position(idx + 1) that letter shows
ONLY 1 letter can show up

input: list of strings
output: int - number of valid passwords

thoughts: maybe need to consider if position is out of bounds?
"""
def new_valid_password(passwords):
    separate_parts(passwords)
    min_max(passwords)
    target_letter(passwords)
    valid = 0
    for password in passwords:
        counter = 0
        policy, letter, check_password = password
        pos1, pos2 = policy #idx = pos - 1
        idx1 = pos1 - 1
        idx2 = pos2 - 1
        if idx1 in range(0, len(check_password)) and check_password[idx1] == letter:
            counter += 1
        if idx2 in range(0, len(check_password)) and check_password[idx2] == letter:
            counter += 1
        if counter == 1:
            valid += 1
        # else:
        #     print('invalid password', password)
    return valid

# print(new_valid_password(example)) #1 valid password: 2 and 3 are invalid
print(new_valid_password(passwords_input))
