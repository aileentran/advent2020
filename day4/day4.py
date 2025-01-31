"""
Day 4: Passport Processing
input: convert file to dictionary w/ key:value pairs
output: int - number of valid passports

Part 1
valid passport = need to have everything except for cid (country id)
cid is optional or else.. we be stranded
"""

def open_file(file_name):
    file = open(file_name, 'r')
    passports = []
    passport = {}
    for line in file:
        line = line.rstrip('\n')
        info = line.split(' ')
        if info[0] == '':
            passports.append(passport)
            passport = {}
        else:
             passport.update(filling_passport(info))
    passports.append(passport) #add the very last passport
    file.close()
    return passports

def filling_passport(info):
    passport = {}
    for i in info:
        fields = i.split(':')
        field, data = fields
        passport[field] = data
    return passport

example = open_file('example.txt')
input = open_file('input.txt')

def passport_processing(passports):
    valid = 0
    for passport in passports:
        if len(passport) == 8:
            valid += 1
            continue
        if 'cid' not in passport.keys() and len(passport) == 7:
            valid += 1
    return valid

# print(passport_processing(example))
# print(passport_processing(input))

"""
Part 2
stricter rules!
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""
def strict_processing(passports):
    valid = 0
    for passport in passports:
        if (len(passport) == 7 and 'cid' not in passport.keys()) or len(passport) == 8:
            if check_valid(passport) == True:
                valid += 1
    return valid

def check_valid(passport):
    if int(passport['byr']) not in range(1920, 2003):
        return False
    if int(passport['iyr']) not in range(2010, 2021):
        return False
    if int(passport['eyr']) not in range(2020, 2031):
        return False

    # print(passport['hgt'])
    measurement = passport['hgt'][-2:]
    # print('measurement', measurement)
    if measurement != 'cm' and measurement != 'in':
        print('invalid measurement!', measurement)
        return False

    number = int(passport['hgt'][:-2])

    if measurement == 'cm' and number not in range(150, 194):
        return False
    if measurement == 'in' and number not in range(59, 76):
        return False

    if passport['hcl'][0] != '#' or len(passport['hcl']) != 7:
        return False

    for char in passport['hcl'][1:]:
        if char.isnumeric() and int(char) not in range(10):
            return False
        elif char.isnumeric() == False and char not in map(chr, range(ord('a'), ord('g'))):
            return False

    valid_eyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if passport['ecl'] not in valid_eyecolors:
        return False

    if passport['pid'].isnumeric() == False or len(passport['pid']) != 9:
        return False
    return True

print(strict_processing(example))
print(strict_processing(input))
