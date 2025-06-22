function Rectangle(width, height) {
    this.width = width;
    this.height = height;

    this.area = function() {
        return this.width * this.height;
    };

    this.perimeter = function() {
        return 2 * (this.width + this.height);
    };
}
const rect1 = new Rectangle(10, 5);
const rect2 = new Rectangle(7, 3);
console.log(`Area of rect1: ${rect1.area()} square units`);
console.log(`Perimeter of rect1: ${rect1.perimeter()} units`);
console.log(`Area of rect2: ${rect2.area()} square units`);
console.log(`Perimeter of rect2: ${rect2.perimeter()} units`);
