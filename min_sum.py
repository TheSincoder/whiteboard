# Given a 2D ( nested ) list of size m * n, 
# your task is to find the sum of the minimum values in each row.

# For Example:

from re import T


a_list=[
  [ 1, 2, 3, 4, 5 ],        #  minimum value of row is 1
  [ 5, 6, 7, 8, 9 ],        #  minimum value of row is 5
  [ 20, 21, 34, 56, 100 ]   #  minimum value of row is 20
]

# So the function should return 26 because the sum 
# of the minimums is 1 + 5 + 20 = 26.

# Note: You will always be given a non-empty list containing 
# positive values.

def min_sum():
  x = min(a_list[0])
  y = min(a_list[1])
  z = min(a_list[2])
  t = x + y + z
  return t

print(min_sum())

b_list = []
def min_sum(a_list):
  for i in a_list:
    b_list.append(min(i))
  return sum(b_list)

print(min_sum(a_list))

def sm(a_list):
  return sum(map((lambda x: min(x)), a_list))

print(sm(a_list))