# Electric Company
# Create a function that given a list which represents street lights 
# given as a parameter, determine if an outage has occurred. 
# A street with a total number of "F" greater than or equal to 2 returns "Outage", 
# anything below returns "Power"
# Example Input: [ 'T', 'F', 'F', 'F' ]
# Example Output: "Outage"

# thought process:
# create a function for street lights
# F >= 2 returns Outage
# F < 2 returns Power
# count the amount of times F shows up in a list

def street_lights(status):
    x = status.count('F')
    if x >= 2:
        return "Outage"
    else:
        return "Power"

print(street_lights([ 'T', 'F', 'T', 'T', 'T' ]))

new_list = []
def power(status_list):
    for letter in status_list:
        if letter == 'F':
            new_list.append(letter)
    
    if len(new_list) >= 2:
        return "Outage"
    else:
        return "Power"

print(power([ 'T', 'F', 'F', 'T', 'T' ]))


