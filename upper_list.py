# Write a function that takes a single string as argument. 
# The function must return an ordered list containing the indexes 
# of all capital letters in the string.
ex = "caN yOu FInD me"
# output: [2,5,8,9,11]


# for i in range(len(string)):
    #if i = i.upper():
        #append the index to a_list

a_list = []
def upper_index(x):
    for i in x:
        if i == i.upper() and i != ' ':
            a_list.append(x.index(i))
                    
    return a_list
print(upper_index(ex))