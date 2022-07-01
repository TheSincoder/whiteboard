// Let's play rock paper scissors! 
// You have to return which player won! 
// In case of a draw return Draw!.

// Examples:

// rps('scissors','paper') // Player 1 won!
// rps('scissors','rock') // Player 2 won!
// rps('paper','paper') // Draw!

// rock : scissors
// scissors beats paper
// paper beats rock

let rock = 'rock'
let paper = 'paper'
let scis = 'scissors'

function rps(x,y){
    if(x == y){
        return 'draw'
    }else if((x== rock && y == scis)||(x== scis && y == rock)){
        return 'rock beats scissors'
    }else if((x== scis && y == paper)||(x==paper && y == scis)){
        return 'scissors beats paper'
    }else if((x==paper && y == rock)||(x == rock && y== paper)){
        return 'paper beats rock'
    }

}

console.log(rps(rock,rock))