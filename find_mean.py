# Return the "centered" average of an array of ints, 
# which we'll say is the mean average of the values, 
# except ignoring the largest and smallest values in the array. 
# If there are multiple copies of the smallest value, remove all copies
# and likewise for the largest value. 
# return the smallest whole number integer average
# You may assume that the array is length 3 or more.

# Input
nums1=[1, 2, 3, 4, 100]
# Outputs:
# 3

# Input
nums2=[1, 1, 5, 5, 10, 8, 7]
# Outputs:
# 6

# Input
nums3=[-10, -4, -2, -4, -2, 0]
# Outputs:
# -3

from statistics import mean
array=[]

def find_mean(x):
    for i in x:
        if i != min(x) and i != max(x):
            array.append(i)
    return int(mean(array))

print(find_mean(nums1))
