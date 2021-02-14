// Day 6: Bitwise Operators
function getMaxLessThanK(n,k){
    var max = 0;
    for(let i = 1 ; i < n+1 ; i++){
        for(let j = i+1 ; j < n+1 ; j++){
            if(((i&j) > max) && ((i&j) < k)) {
                max = (i&j);
            }
        }
    }
    return max;
}

// Day 6: JavaScript Dates
function getDayName(dateString) {
    const weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    
    return weekdays[new Date(dateString).getDay()];
}