// 1. indexOf(value) – უკან აბრუნებს პირველი ემოცირებული ელემენტის ინდექსს მასივში, თუ არაა, -1-ს აბრუნებს
let arr1 = [1,2,3,2,4];
console.log(arr1.indexOf(2)); // 1
console.log(arr1.indexOf(5)); // -1
console.log(arr1.indexOf(2, 2)); // 3 (ძებნა იწყება ინდექსი 2–დან)

// 2. lastIndexOf(value) – უკან აბრუნებს ბოლო ემოცირებული ელემენტის ინდექსს
let arr2 = [1,2,3,2,4];
console.log(arr2.lastIndexOf(2)); // 3
console.log(arr2.lastIndexOf(1)); // 0
console.log(arr2.lastIndexOf(5)); // -1

// 3. includes(value) – აბრუნებს true თუ ელემენტი არსებობს მასივში, false თუ არა
let arr3 = [1,2,3,4];
console.log(arr3.includes(3)); // true
console.log(arr3.includes(5)); // false
console.log(arr3.includes(1)); // true
