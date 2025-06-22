// 1. შექმენით Car კონსტრუქტორის ფუნქცია, რომელიც არგუმენტად მიიღებს მანქანის მარკას, მოდელს და წელს, შემდეგ კი მათი მეშვეობით შექმენით ახალი ობიექტი.
// 2. Car ობიექტის კონსტრუქტორს დაუმატეთ მეთოდი getDescription, რომელიც დააბრუნებს სტრინგს, რომელიც გააერთიანებს მანქანის მარკას, მოდელს და წელს.
// 3. უკვე შექმნილი კონსტრუქტორის მეშვეობით შექმენით სამი განსხვავებული Car ობიექტი და გამოიტანეთ მათი აღწერილობები getDescription მეთოდის გამოყენებით.
// 4. გააფართოვეთ Car კონსტრუქტორი age მეთოდის დამატებით, რომელიც გამოითვლის მანქანის ასაკს ახლანდელი წლის მიხედვით.
// 5. შექმენით Rectangle კონსტრუქტორი, რომელიც არგუმენტად მიიღებს მართკუთხედის სიგანეს და სიმაღლეს, ასევე დაუმატეთ მეთოდები მისი ფართობის და პერიმეტრის გამოსათვლელად.

function Car(brand, model, year) {
    this.brand = brand;
    this.model = model;
    this.year = year;

    this.getDescription = function() {
        return `Car: ${this.brand} ${this.model}, Year: ${this.year}`;
    };

    this.age = function(currentYear) {
        return currentYear - this.year;
    };
}
const car1 = new Car("Toyota", "Camry", 2015);
const car2 = new Car("Honda", "Civic", 2018);
const car3 = new Car("Ford", "Mustang", 2020);
console.log(car1.getDescription());
console.log(car2.getDescription());
console.log(car3.getDescription());
console.log(`Age of car1: ${car1.age(2025)} years`);
console.log(`Age of car2: ${car2.age(2025)} years`);
console.log(`Age of car3: ${car3.age(2025)} years`);


