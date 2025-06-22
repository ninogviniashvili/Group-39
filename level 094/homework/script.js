//1

let number = 0;

while (number <= 20) {
    console.log(number);
    number += 2;
}
 


//2 

let num = 10;

while (num >= 1) {
    console.log(num);
    num -= 1;
}



// 3

let totalCount = 0;

while (count <= 5) {
    totalCount++;
    count++;
}

console.log("Total count from 1 to 5 is:", totalCount);



//4

let numb = 1;

while (numb <= 100) {
    console.log(numb);
    numb *= 2;
}



//5

let userInput = prompt("Please enter a number:");
let nu = 1;
let limit = parseInt(userInput);

while (nu <= limit) {
    console.log(nu);
    nu++;
}



// 1

for (let i = 1; i <= 10; i++) {
    console.log(`Square of ${i} is ${i * i}`);
}



// 2

for (let i = 1; i <= 50; i++) {
    console.log(i);
}



// 3

const names = ['ana', 'ben', 'carl', 'dana', 'eva'];
for (let i = 0; i < names.length; i++) {
    console.log(`გამარჯობა, ${names[i]}!`);
}



// 4

for (let i = 100; i >= 0; i -= 10) {
    console.log(i);
}


// 5

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let sum = 0;

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0) {
        sum += numbers[i];
    }
}

console.log("Sum of even numbers:", sum);
