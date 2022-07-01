#Write a function that accepts an array of 10 integers (between 0 and 9), that 
# returns a string of those numbers in the form of a phone number.

def create_phone_number(n):
    x ='('
    for num in range(len(n)):
        x += str(n[num])
        if num == 2:
            x += ') '
        elif num == 5:
            x += '-'
    return x