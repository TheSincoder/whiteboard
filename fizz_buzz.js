// Using an arrow function
// Write a program that prints the numbers from 1 to n 
// and for multiples of '3' print "Fizz" instead of the 
// number and for the multiples of '5' print "Buzz". For 
// multiples of 3 and 5, print fizzbuzz

// In Python:
// def fizz_buzz():
//     for number in range(1,21):
//         if number % 3 == 0 and number % 5 == 0:
//             print("FizzBuzz")
//         elif number % 5 == 0:
//             print("Buzz")
//         elif number % 3 == 0:
//             print("Fizz")
//         else:
//             print(number)

// fizz_buzz()

fizzBuzz=(n) => {
    for (let number = 1; number <= n; number ++){
        if (number % 3 == 0 && number % 5 == 0){
            console.log("FizzBuzz");
        }else if (number % 5 ==0){
            console.log("Buzz");
        }else if(number % 3 == 0){
            console.log("Fizz");
        }else{console.log(number);}
    };    
};

fizzBuzz(20)