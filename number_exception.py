# There is an array with some numbers. 
# All numbers are equal except for one. Try to find it!
# It's guaranteed that array contains at least 3 numbers.

# ex: [ 1, 1, 1, 2, 1, 1 ] solution - 2
# ex: [ 0, 0, 0.55, 0, 0 ] solution - 0.55

# create a function that returns the unequal number
# check which numbers in a list are equal to each other
# pick out the unequal one and return it

def array(a_list):
    a_set = set(a_list)
    for n in a_set:
        if a_list.count(n) == 1:
            return n
        

print(array([ 1, 1, 1, 2, 1, 1 ]))