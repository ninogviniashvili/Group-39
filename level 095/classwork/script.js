// შექმენით person კონსტრუქტორი კუთვნილებებით - name, lastname, age.
//  შემდეგ მისი მეშვეობით შექმენით 3 ობიექტი.

function Person(name, lastname, age) {
    this.name = name;
    this.lastname = lastname;
    this.age = age;
}

const person1 = new Person("Nino", "gv", 13);
const person2 = new Person("Mari", "ch", 14);
const person3 = new Person("Mari", "Gel", 13);

console.log(person1);
console.log(person2);    
console.log(person3);
