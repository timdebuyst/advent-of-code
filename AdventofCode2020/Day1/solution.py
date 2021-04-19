# Day 1: Report Repair
# Part 1

#############################

# Step 1: get input values from input.txt
input_file = open("input.txt", "r")
input_strings = input_file.readlines()
#print(input_strings)

#test = input_strings[0]
#print(test[:-2])

# format input list
input_ints = [int(x.replace('\n', '')) for x in input_strings]
#input_ints = [int(x[:-1]) for x in input_strings] # other possibility
#print(input_ints)

# Step 2: find two entries that sum up to 2020
# use brute force (maybe optimization possible?)
solution_found = False
for x in input_ints:
    for y in input_ints:
        if x + y == 2020:
            print(f"Solution found for part 1: {x*y}")
            solution_found = True
            break
    if solution_found:
        break

#############

# Part 2

# Step 3: find three entries that sum up to 2020
# use brute force (maybe optimizaton possible?)
solution_found = False
for x in input_ints:
    for y in input_ints:
        for z in input_ints:
            if (x==y or x==z or y==z): # assume no doubles, and no doubles allowed in solution
                break
            if x + y + z == 2020:
                print(f"Solution found for part 2: {x*y*z}")
                solution_found = True
                break
        if solution_found:
            break
    if solution_found:
        break
