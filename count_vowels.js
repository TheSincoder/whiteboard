// Return the number (count) of vowels in the given string.
// We will consider a, e, i, o, u as vowels (but not y).
// The input string will only consist of lower case letters and/or spaces.
inputString="hey there you fine beautiful people"

function vowelCounter(input){
    count = 0
    for (letter of input){
        if (letter == 'a'|| letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u'){
            count += 1
        };
    }return count
}

console.log(vowelCounter(inputString))