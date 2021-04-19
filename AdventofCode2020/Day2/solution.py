# Day 2: Password Philosophy
# Part 1

input_file = open("input.txt", "r")
input_strings = input_file.readlines()
input_strings = [x[:-1] for x in input_strings]
#print(input_strings)

valid_amount = 0
for input in input_strings:
    info = input.split(" ") # first is the range of required amounts, second is the required letter, third is the password
    #print(info) 
    min, max = info[0].split("-")
    min = int(min)
    max = int(max)
    letter = info[1][:-1]
    pwd = info[2]

    count = 0
    for x in pwd:
        if x == letter:
            count += 1
    
    if count >= min and count <= max:
        valid_amount += 1

print(f"Part 1: The amount of correct passwords is: {valid_amount}")

# Part 2

valid_amount = 0
for input in input_strings:
    info = input.split(" ")
    pos1, pos2 = info[0].split("-")
    pos1 = int(pos1) - 1
    pos2 = int(pos2) - 1
    letter = info[1][:-1]
    pwd = info[2]

    if pwd[pos1] == letter or pwd[pos2] == letter:
        if not (pwd[pos1] == letter and pwd[pos2] == letter):
            valid_amount += 1

print(f"Part 2: The amount of correct passwords is: {valid_amount}")