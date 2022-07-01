# Least Larger
# Given an array of numbers and an index, return the index of the least number
# larger than the element at the given index, or -1 if there is no such index.
# Example:
# input= [4, 1, 3, 5, 6]
# Output: 3
# Input: ([4, 1, 3, 5, 6], 4)
# Output: -1

def least_larger(a_list, index):
    num = a_list[index]
    for i in a_list:
        if i == num + 1:            
            return a_list.index(i)
      
    return -1



print(least_larger([4, 1, 3, 5, 6], 4))

def leastLarger(arr, i):
    return -1 if max(arr)==arr[i] else arr.index(sorted(arr)[sorted(arr).index(arr[i])+1])