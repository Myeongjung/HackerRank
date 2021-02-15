// Day 9: Binary Calculator
function action(e) {
    var btn = e.target || e.srcElement;
    var input = document.getElementById(btn.id).innerHTML;
    var res = document.getElementById('res');
    
    switch(input) {
        case 'C':
            res.innerHTML = '';
            break;
        case '=':
            var expr = res.innerHTML;
            var nums = /(\d+)/g;

            expr = expr.replace(nums, function(match) {
                return parseInt(match, 2);
            })
            
            res.innerHTML = eval(expr).toString(2);
            break;
        default:
            res.innerHTML += input;
            break;
    }
}
var buttons = document.getElementsByTagName('button');
for (let button of buttons) {
    button.onclick = action;
}

// CSS
body {
  width: 33%;
}

#res {
  background-color: lightgray;
  border: solid;
  height: 48px;
  font-size: 20px;
}

#btns button {
  width: 25%;
  height: 36px;
  font-size: 18px;
  margin:0;
  float: left;
}

#btn0, #btn1 {
  background-color: lightgreen;
  color: brown;
}

#btnClr, #btnEql {
  background-color: darkgreen;
  color: white;
}

#btnSum, #btnSub, #btnMul, #btnDiv {
  background-color: black;
  color: red;
}

//html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Binary Calculator</title>
        <link rel="stylesheet" href="css/binaryCalculator.css" type="text/css">
    </head>
    <body>       
        <div id="res"></div>
        <div id="btns">
            <button id="btn0" onclick="clickZero()">0</button>
            <button id="btn1" onclick="clickOne()">1</button>
            <button id="btnClr" onclick="clickClear()">C</button>
            <button id="btnEql" onclick="clickEql()">=</button>
            <button id="btnSum" onclick="clickSum()">+</button>
            <button id="btnSub" onclick="clickSub()">-</button>
            <button id="btnMul" onclick="clickMul()">*</button>
            <button id="btnDiv" onclick="clickDiv()">/</button>
        </div>
        
        <script src="js/binaryCalculator.js" type="text/javascript"></script>
    </body>
</html>