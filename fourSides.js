// You are given the length and width of a 4-sided polygon. 
// The polygon can either be a rectangle or a square.
// If it is a square, return its area. If it is a rectangle, 
// return its perimeter.

// area_or_perimeter(6, 10) --> 32
// area_or_perimeter(3, 3) --> 9

function fourSides(x,y){
    if(x == y){
        return x*y
    }else{
    let l = x*2
    let w = y*2
    return l + w
    }
}

console.log(fourSides(6,6))

const perimeter =(x,y)=>{return x === y? x*y:x*2 + y*2}

console.log(perimeter(6,6))