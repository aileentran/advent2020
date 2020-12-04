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

def passport_processing(passport):
    return


print(passport_processing(example))
# print(passport_processing()) actual input!
