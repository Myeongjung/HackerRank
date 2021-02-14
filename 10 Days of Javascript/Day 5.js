// Day 5: Inheritance
Rectangle.prototype.area = function(){
    return this.w * this.h;
}

class Square extends Rectangle{
    constructor(w){
        super(w,w);
    }
}

// Day 5: Template Literals
function sides(literals, ...expressions) {
    var area = expressions[0];
    var perimeter = expressions[1];
    
    var s1 = (perimeter + Math.sqrt(perimeter**2 - (16*area)))/4;
    var s2 = (perimeter - Math.sqrt(perimeter**2 - (16*area)))/4;
    
    return [s1, s2].sort();
}

// Day 5: Arrow Functions
function modifyArray(nums) {
    return (nums.map(num => (num%2==0)?num*2:num*3))
}