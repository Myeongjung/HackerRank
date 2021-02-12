// Day 2: Conditional Statements: If-Else
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getGrade(score) {
    let grade;
    
    if(score <= 5){
        grade = 'F'
    }else if(score <= 10){
        grade = 'E'
    }else if(score <= 15){
        grade = 'D'
    }else if(score <= 20){
        grade = 'C'
    }else if(score <= 25){
        grade = 'B'
    }else {
        grade = 'A'
    }
    return grade;
}
    
// Day 2: Conditional Statements: Switch
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getLetter(s) {
    let letter;
    switch(true){
        case 'aeiou'.includes(s[0]):
            letter = 'A';
            break;
        case 'bcdfg'.includes(s[0]):
            letter = 'B';
            break;
        case 'hjklm'.includes(s[0]):
            letter = 'C';
            break;
        default:
            letter = 'D';
            break;
    }
        
    return letter;
}

// Day 2: Loops
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function vowelsAndConsonants(s) {
    for(var i of s) {
        if(/[aeiou]/.test(i)){
            console.log(i);
        }
    }
    
    for(var j of s) {
        if(!/[aeiou]/.test(j)){
            console.log(j);
        }
    }
}


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}