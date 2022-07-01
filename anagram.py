#Given two strings, return true if they are anagrams of eachother, and false otherwise.
s1 = "anagram"
t1 = "nagaram"
# Output:
# True
s2 = "rat"
t2 = "car"
#Output:
# False

# create a function to look for anagrams
# use set or sort methods to compare
# Return a boolean 

# doesn't account for mismatched duplicate letters
def anagram(x, y):
    if set(x) == set(y):
        return True
    else: 
        return False

print(anagram(s1, t1))

def anagram(x, y):
    if sorted(x) == sorted(y):
        return True
    else: 
        return False
    

print(anagram(s1, t1))

def is_anagram(s,t):
    from collections import Counter 
    return Counter(s)==Counter(t)
print(is_anagram(s1, t1))

