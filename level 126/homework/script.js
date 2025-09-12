// JavaScript-ში ორი ძირითადი ტიპის მეხსიერება არსებობს:

// 1. Primitive types (პირველადი ტიპები)
// ისინი ინახება პირდაპირი მნიშვნელობით
let num = 42;        // Number
let str = "hello";   // String
let bool = true;     // Boolean

// 2. Reference types (რეფერენციის ტიპები)
// ცვლადი ინახავს მისამართს, actual მონაცემები heap-ში ინახება
let obj = {name: "Nino", age: 20}; // Object
let arr = [1,2,3];                 // Array
let func = function() { return 1; }; // Function
let date = new Date();              // Date
let map = new Map();                // Map
let set = new Set();                // Set

//2
// 1. Hoisting (ჰოისტინგი)
// JS-ში ფუნქციები და ცვლადები (var) "წინ წაიწევს" კოდის თავში კომპაილის ეტაპზე.
// ამის გამო შეგიძლია გამოიყენო ფუნქცია ან ცვლადი გამოცხადებამდე.


// 2. Scope (სკოპი)
// სკოპი განსაზღვრავს სად არის ცვლადი ხელმისაწვდომი.
// არსებობს: 
// - Global scope: გვერდის ნებისმიერ ადგილიდან წვდომა
// - Local / Function scope: მხოლოდ ფუნქციის შიგნიდან
// - Block scope: მხოლოდ ბლოკის { } შიგნიდან (let/const)