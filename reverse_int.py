# Given an integer return the integer with all the digits reversed:
# Must work for positive and negative numbers
# Input
x1=1234
# Output
# 4321
# Input
x2=-1234
# Output
# -4321

def reverse(x):
    # turn it into a string
    # sort the list in reverse
    # turn it back into an integer
    z = ''
    
    if x >= 0:
        y = str(x)
        for i in y[::-1]:
            z += i
        return int(z)
    else:
        y = str(abs(x))
        for i in y[::-1]:
            z += i
        return int(z)* -1
        

print(reverse(x1))