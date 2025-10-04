// 1. Use push to add "orange" to the array ["apple", "banana"].\

let fruits = ["apple", "banana"];
fruits.push("orange");
console.log(fruits); 

// 2. Use pop to remove the last element from the array ["cat", "dog", "bird"].
let animals = ["cat", "dog", "bird"];
animals.pop();
console.log(animals);


// 3. Use shift to remove the first element from the array ["red", "green", "blue"].
let colors = ["red", "green", "blue"];
colors.shift();
console.log(colors); 


// 4. Use unshift to add "Monday" at the beginning of the array ["Tuesday", "Wednesday"].
let days = ["Tuesday", "Wednesday"];
days.unshift("Monday");
console.log(days); 


// 5. Use concat to merg e the arrays [1, 2, 3] and [4, 5, 6].
let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];
let merged = arr1.concat(arr2);
console.log(merged);