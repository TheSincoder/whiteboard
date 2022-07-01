# Write a Python program to add the digits of a positive integer 
# repeatedly until the result has a single digit.
# The input number will be greater than 0

# EX
# Input:
n1=48
# 4+8=12
# 1+2=3
# Output:
# 3

# Input
n2=59
# Output
# 5
n3=489

def single(x):
    while True:
        if len(str(x)) > 1:
            y = x//10
            z = x%10
            x = y + z
            
        else:
            return x
        
    

print(n1%9)
print(single(n3))