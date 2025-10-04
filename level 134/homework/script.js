// 1. Take the array [1, 2, 3, 4, 5] and return a new array where each number is doubled if it’s even, otherwise leave it as is.
let numbers = [1, 2, 3, 4, 5];
let doubledEvens = numbers.map(num => num % 2 === 0 ? num * 2 : num);
console.log(doubledEvens);

// 2. Given the array ["cat", "elephant", "dog"], return an array with the first letter of each string.
let animals = ["cat", "elephant", "dog"];
let firstLetters = animals.map(word => word[0]);
console.log(firstLetters);

// 3. From ["alice", "bob", "charlie"], return a new array of names where only the first letter is capitalized.
let names = ["alice", "bob", "charlie"];
let capitalized = names.map(name => name[0].toUpperCase() + name.slice(1));
console.log(capitalized);

// 4. For the array [10, 20, 30], return a new array of strings in the form "Index: X, Value: Y".
let values = [10, 20, 30];
let indexValueStrings = values.map((value, index) => `Index: ${index}, Value: ${value}`);
console.log(indexValueStrings);


// 5. From the array [{id:1, name:"apple"}, {id:2, name:"banana"}, {id:3, name:"cherry"}], return a new array containing only the name values in uppercase.
let items = [
  {id: 1, name: "apple"},
  {id: 2, name: "banana"},
  {id: 3, name: "cherry"}
];

let upperNames = items.map(item => item.name.toUpperCase());
console.log(upperNames);

