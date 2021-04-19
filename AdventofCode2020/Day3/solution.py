# Day 3: Toboggan Trajectory
# Part 1

# get input
input_file = open("input.txt", "r")
input_strings = input_file.read().split("\n")
l = len(input_strings[0]) # 31

# right 3, down 1
num_trees = 0
slope_step = 0
for x in input_strings:
    if x == "":
        break # end of list
    if x[slope_step] == '#': # its a tree
        num_trees += 1
        x = x[:slope_step] + 'X' + x[slope_step+1:]
    else: # its not a tree
        x = x[:slope_step] + 'O' + x[slope_step+1:]
    print(x)
    slope_step += 3
    slope_step %= l

print(num_trees)
print("\n")

# Part 2

def find_num_trees(input_strings, right, down, printthis):
    l = len(input_strings[0]) # 31
    pos = 0
    num_trees = 0
    for i, x in enumerate(input_strings):
        if x == "":
                break # end of list
        if i % down == 0: # on the right row
            if x[pos] == '#': # its a tree
                num_trees += 1
                if printthis: 
                    x = x[:pos] + 'X' + x[pos+1:]
            else: # its not a tree
                if printthis: 
                    x = x[:pos] + 'O' + x[pos+1:]
            if printthis: 
                print(x)
            pos += right
            pos %= l
        else: # row needs to be skipped
            if printthis:
                print(x)
    
    return num_trees

sol1 = find_num_trees(input_strings, 1, 1, False)
sol2 = find_num_trees(input_strings, 3, 1, False)
sol3 = find_num_trees(input_strings, 5, 1, False)
sol4 = find_num_trees(input_strings, 7, 1, False)
sol5 = find_num_trees(input_strings, 1, 2, False)
print(sol1)
print(sol2)
print(sol3)
print(sol4)
print(sol5)
print("\n")
print(sol1*sol2*sol3*sol4*sol5)