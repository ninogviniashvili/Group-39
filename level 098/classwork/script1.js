// 2. ეცადეთ რომ შექმნათ person კონსტრუქტორი, name, age, lastname კუთვნილებებით.

// შემდეგ html-ში გქონდეთ ღილაკი, რომელზეც გექნებათ მიბმული ფუნქცია, რომელიც შექმნის ახალ person 
// ობიექტს და გამოიტანს კონსოლში.
function Person(name, age, lastname) {
    this.name = name
    this.age = age
    this.lastname = lastname

    this.introduce = function() {
        return `My name is ${this.name} ${this.lastname}, I am ${this.age} years old.`;
    }
}