// Day 3: Arrays
function getSecondLargest(nums) {
    var max;  
    for (var e of nums.sort((x, y)=> x<y)){
        if(max == null){
            max = e
        }else if(max > e){
            return e
        }
    }
}

// Day 3: Try, Catch, and Finally
function reverseString(s) {
    var str = "";
    try{
        console.log(s.split("").reverse().join(""))
    }catch(e){
        console.log(e.message);
        console.log(s);
    }
}

// Day 3: Throw
function isPositive(a) {
    if(a < 0){
        throw new Error("Negative Error")
    }else if(a == 0){
        throw new Error("Zero Error")
    }
    return "YES"
}
