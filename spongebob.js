// Remember the spongebob meme that is meant to make fun of people 
// by repeating what they say in a mocking way?

// You need to create a function that converts the input into this 
// format, with the output being the same string expect there is a pattern of uppercase and lowercase letters.

// Examples:

// spongeMeme("stop Making spongebob Memes!") // => 'StOp mAkInG SpOnGeBoB MeMeS!'

let sen = "stop Making spongebob Memes!";

    function spongeBob(x){
        newString=""
        for (i=0; i<=x.length-1;i++){
            if (i % 2 == 0){
                newString += x[i].toUpperCase()
            }else{newString += x[i].toLowerCase()}
        };
        return newString
    };

console.log(spongeBob(sen))