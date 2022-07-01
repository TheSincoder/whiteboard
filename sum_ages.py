# Given the following list of people, use the map function 
# to sum all the age of all the people in the class

my_list=[
    {"Name":"Kevin",
    "Age":36,
    "Weight":220
    },
    {"Name":"Brian",
    "Age":27,
    "Weight":190
    },
    {"Name":"John",
    "Age":30,
    "Weight":180
    },
    {"Name":"Tony",
    "Age":23,
    "Weight":150
    },
    {"Name":"David",
    "Age":24,
    "Weight":150
    }
]

# use map faction
# locate the value of ages
# return the ages

f = list(map(lambda x: my_list[0]['Age'] + my_list[1]['Age'] + my_list[2]['Age'] + my_list[3]['Age'] + my_list[4]['Age'], my_list))
print(f[0])

a = sum(map(lambda age: age["Age"] , my_list))
print(a)
