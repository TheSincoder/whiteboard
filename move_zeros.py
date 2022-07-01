# Move Zeros
# Given an array nums, write a function to move all 0's to the end 
# of it while maintaining the relative order of the non-zero elements.
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example Input: [0,0,11,2,3,4]
# Example Output: [11,2,3,4,0,0]

# create a function to remove the 0s
# create a new list and .append() the non zero values into it
# return the new list
# create variables for examples

x1 =  [0,1,0,3,12]
x2 =  [1,3,12,0,0]
x3 = [0,0,11,2,3,4]
x4 = [11,2,3,4,0,0]


# move the zeros to the end
def move_zeros(a_list):
    for n in a_list:
        if n== 0: 
            a_list.append(a_list.pop(a_list.index(0)))
    return(a_list)

print(move_zeros(x1))


# removes the zeros
new_list = []

def remove_zeros(a_list):
    for i in a_list:
        if i == 0:
            continue
        else:
            new_list.append(i)
    return new_list

print(remove_zeros(x4))

