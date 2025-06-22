// ობიექტი არის მონაცემების ერთიანი ერთეული, რომელიც შეიცავს კუთვნილებებს და ფუნქციებს (მეთოდებს).
// კუთვნილება (property) არის ობიექტის ცალკეული მახასიათებელი, როგორიცაა სახელი, გვარი და ასაკი.
// მეთოდი (method) არის ფუნქცია, რომელიც განსაზღვრულია ობიექტის შიგნით.

const me = {
  name: "nino",
  surname: "gv",
  age: 13
};

const brother = {
  name: "luka",
  surname: "gv",
  age: 23
};


console.log(me);
console.log(brother);


console.log(me.name);
console.log(me.surname);
console.log(me.age);

console.log(brother.name);
console.log(brother.surname);
console.log(brother.age);


me.age = 26;
brother.name = "luka";

console.log(me);
console.log(brother);


me.hobby = "reading";
brother.hobby = "sports";

console.log(me);
console.log(brother);


delete me.surname;
delete brother.age;

console.log(me);
console.log(sister);


const userName = prompt("enter name:");
const userSurname = prompt("enter surname:");
const userAge = prompt("enter age:");


const user = {
  name: userName,
  surname: userSurname,
  age: userAge
};

console.log(user);

user.name = "change name";

console.log(user);