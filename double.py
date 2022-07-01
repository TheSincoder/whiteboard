# Check if Number and its double exists
# Given an array arr of integers, check if there exists two integers N and M 
# such that N is the double of M ( i.e. N = 2 * M).
# Example 1:
arr1 = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,
# that is, 10 = 2 * 5.
# Example 2:
arr2 = [7,1,14,11]
# Output: true
# Explanation: N = 14 is the double of M = 7,
# that is, 14 = 2 * 7.
# Example 3:
arr3 = [3,1,7,11]
# Output: false
# Explanation: In this case does not exist N and M, 
# such that N = 2 * M.

# check through the list of the numbers for a double of another number. 

def check_double(array):
    new_array = array
    x = bool
    for i in array:
        if i * 2 in new_array:
            x = True
    if x == True:
        return x
    else:
        x = False
        return x
    


print(check_double(arr2))

def check_double(array):
    new_array = array
    x = bool
    for i in array:
        if i * 2 in new_array:
            x = True
    if x == True:
        return x
    else:
        x = False
        return x
    


print(check_double(arr2))