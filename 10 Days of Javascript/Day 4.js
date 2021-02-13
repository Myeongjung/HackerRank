// Day 4: Create a Rectangle Object
function Rectangle(a, b) {
    this.length = a;
    this.width = b;
    this.perimeter = 2*(a+b);
    this.area = a*b
}

// Day 4: Count Objects
function getCount(objects) {
    return objects.filter(object =>object.x===object.y).length;
}

// Day 4: Classes
class Polygon{
    constructor(inputs){
        this.perimeters = inputs;
    }
    perimeter() {
        return this.perimeters.reduce(function add(a,b){return a+b;})
    }
}