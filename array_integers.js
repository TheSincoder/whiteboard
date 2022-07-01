//  Given an array of integers.
//  Return an array, where the first element is the count of positives numbers 
//  and the second element is sum of negative numbers.
//  If the input array is empty or null, return an empty array.
//  Example
input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15] 
//  you should return [10, -65].

function countSum(x){
    posNum = []
    negNum = []
    newArr = []
    count = 0
    z= 0
    for (i=0; i<=x.length-1;i++){
        if (x[i] > 0){
            posNum.push(x[i])
        }else if (x[i] < 0) {
            negNum.push(x[i])
        }
    };
    console.log(posNum)
    console.log(negNum)
    y = posNum.length
    console.log(y)
    
    z = negNum.reduce((accumulator, current)=>{return accumulator + current})
    console.log(z)
    newArr = [y,z]
    console.log(`[${y},${z}]`)
    return newArr
};

console.log(countSum(input))

function doStuff(numbers){
    console.log([numbers.filter(number=>number>-1).length, numbers.filter(number=>number<0).reduce((accumulator, currentNum)=>accumulator+currentNum)]);
};