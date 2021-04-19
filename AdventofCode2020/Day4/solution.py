# Day 4: Passport Processing
# Part 1

from re import match

with open("input.txt", "r") as input_file:
    input_string = input_file.read()
    #print(input_string)
    #input_strings = input_file.readlines() # need to comment out .read() line
    #print(input_strings)

    input_list = input_string.split("\n\n")

    passports = [] # a list of dictionaries
    for x in input_list:
        passport = {}
        y = x.split("\n")
        for z in y:
            key_val_list = z.split(" ")
            for key_val in key_val_list:
                if key_val != "":
                    #print(key_val)
                    key, val = key_val.split(":")
                    passport.update({key : val})
                    #passport[key] = val
        
        passports.append(passport)

    count_valid = 0
    fields_needed = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} # a set, excluding 'cid'
    for passport in passports:
        if 'cid' in passport.keys():
            passport.pop('cid')
        if len(passport.keys()) == len(fields_needed):
            if set(passport.keys()) == fields_needed:
                #print(set(passport.keys()))
                count_valid += 1

    print(f'The answer for part one is: {count_valid}') # this part above is wrong...

    # other try
    count_valid = 0
    for passport in passports: 
        if all([(k in passport) for k in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']]): # excluding 'cid'
            count_valid += 1
    
    print(f'The answer for part one is (other try): {count_valid}')

    # part 2

    count_valid = 0
    for passport in passports: 
        if all([(k in passport) for k in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']]): # excluding 'cid'
            if len(passport['byr']) == 4 and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002:
                if len(passport['iyr']) == 4 and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020:
                    if len(passport['eyr']) == 4 and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030:
                        if ('cm' in passport['hgt'] and int(passport['hgt'][:-2]) >= 150 and int(passport['hgt'][:-2]) <= 193) or ('in' in passport['hgt'] and int(passport['hgt'][:-2]) >= 59 and int(passport['hgt'][:-2]) <= 76):
                            if match('#[0-9a-f]{6}', passport['hcl']):
                                if passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                                    if match('^[0-9]{9}$', passport['pid']):
                                        count_valid += 1

    print(f'The answer for part two is: {count_valid}')