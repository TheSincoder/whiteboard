# Lucky Numbers
# Given an array of integers arr, a lucky integer is an integer which 
# has a frequency in the array equal to its value.
# Return a lucky integer in the array. If there are multiple lucky 
# integers return the largest of them. If there is no lucky integer return -1.
# Example 1:
arr1 = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:
arr2 = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.





def lucky(array):
    lucky_list = []
    
    for i in array:
        if i == array.count(i):
            lucky_list.append(i)
    if lucky_list:
        return f'{max(lucky_list)} is a lucky number'
    else: 
        return -1

print(lucky(arr1))