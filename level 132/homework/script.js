// 1. random

// Generate a random number between 0 and 1
console.log(Math.random());

// Generate a random number between 0 and 10
console.log(Math.random() * 10);

// Generate a random integer between 1 and 100
console.log(Math.floor(Math.random() * 100) + 1);



// 2. floor

// Round 4.7 down to the nearest integer
console.log(Math.floor(4.7)); // 4

// Round a random number between 0 and 10 down to the nearest integer
console.log(Math.floor(Math.random() * 10));

// Round -3.2 down to the nearest integer
console.log(Math.floor(-3.2)); // -4



// 3. Ternary operator

// Check if age is 18 or more
let age = 20;
console.log(age >= 18 ? "Adult" : "Minor");

// Print Even or Odd
let num = 7;
console.log(num % 2 === 0 ? "Even" : "Odd");

// Assign status based on score
let score = 45;
let status = score >= 50 ? "Passed" : "Failed";
console.log(status);



// 4. For loop (JS)

// Print numbers from 1 to 5
for (let i = 1; i <= 5; i++) {
  console.log(i);
}

// Sum numbers from 1 to 10
let sum = 0;
for (let i = 1; i <= 10; i++) {
  sum += i;
}
console.log("Sum:", sum);

// Print each character of "hello"
let word = "hello";
for (let i = 0; i < word.length; i++) {
  console.log(word[i]);
}



// 5. push

// Add apple to the end of fruits array
let fruits = ["banana", "orange"];
fruits.push("apple");
console.log(fruits);

// Add numbers 1, 2, 3 to an empty array
let numbers = [];
numbers.push(1, 2, 3);
console.log(numbers);

// Add JS to skills array
let skills = ["HTML", "CSS"];
skills.push("JS");
console.log(skills);



// 6. pop

// Remove the last item from fruits array
let fruits2 = ["apple", "banana", "cherry"];
fruits2.pop();
console.log(fruits2);

// Remove the last number from [1,2,3,4]
let nums = [1, 2, 3, 4];
nums.pop();
console.log(nums);

// Remove the last element from skills array
let skills2 = ["HTML", "CSS", "JS"];
skills2.pop();
console.log(skills2);



// 7. shift

// Remove the first item from fruits array
let fruits3 = ["apple", "banana", "orange"];
fruits3.shift();
console.log(fruits3);

// Remove the first number from [5,6,7]
let nums2 = [5, 6, 7];
nums2.shift();
console.log(nums2);

// Remove the first element from skills array
let skills3 = ["HTML", "CSS", "JS"];
skills3.shift();
console.log(skills3);



// 8. map

// Multiply each number in [1,2,3] by 2
let arr1 = [1, 2, 3];
let doubled = arr1.map(num => num * 2);
console.log(doubled);

// Add 1 to each number in [4,5,6]
let arr2 = [4, 5, 6];
let added = arr2.map(num => num + 1);
console.log(added);

// Convert each string in ["a","b","c"] to uppercase
let arr3 = ["a", "b", "c"];
let upper = arr3.map(str => str.toUpperCase());
console.log(upper);