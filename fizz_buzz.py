#  Write a function to print all numbers 1 to 20, but there are some constraints
#  If the number is divisible by 3, print 'Fizz' instead of the number
#  If the number is divisible 5, print 'Buzz' instead of the number
#  If the number is divisible by both 3 and 5, print 'FizzBuzz' instead of the number
#  Otherwise, simply print the number

# Function to use the input as an integer and print different strings
# Create if loop to set the paremeters

def fizz_buzz():
    for number in range(1,21):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)

fizz_buzz()

