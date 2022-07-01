#  Write a function that will remove all vowels from a given string. 
#  The function should return a string.
#  Example:
#  Input: 'Joel'
#  Output: 'Jl'

# create a function
# define vowels
# have the function check the list of vowels and match against the string
# only add letters back in to the string that don't match the vowels

def shortcut( s ):

    vowels = ["a","e","i","o","u"]
    answer = ""
    for letter in s:
        if letter.lower() not in vowels:
            answer += letter
    return answer

print(shortcut("JOel"))