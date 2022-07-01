# Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as 
# runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

a_list = [3,1,2,10,1]
new_list = []

def sum(a_list):
    #work through the list
    #add each number to the previous number
    x = 0
    for i in a_list:
        x += i
        new_list.append(x)
    return new_list


print(sum(a_list))

def sum_list(a_list):
    return [sum(a_list[:i+1]) for i in range(len(a_list))]



