const numbers = [1, 2, 3, 4, 5]

for ( const num of numbers){
    console.log(num*3)
}

// 2. Use reduce to console.log the product of all numbers in an array.

const numb = [2, 3, 4, 5]

const product = numb.reduce((acc, num) => acc * num, 1)

console.log(product)

// 3. Use map to create a new array where each number is squared and console.log the new array.

const nums = [1,2,3,4,5]

const squaredNums = nums.map(num => num ** 2)
console.log(squaredNums)

// 4. Use filter to create a new array containing only even numbers and console.log it.

const numberArr = [1,2,3,4,5,6,7,8,9,10]

const evenNumbers = numberArr.filter(num => num %2 ===0)

console.log(evenNumbers)

// 5. Use a for loop to console.log all numbers from 1 to 20.

for (let i = 1 ; i <=20; i++){
    console.log(i)
}


// 6. Use for of to loop through an array of words and console.log only the words that start with a vowel.

const words = ["apple", "banana", "cherry", "orange", "strawberry", "pineapple"]

for (const word of words){
    if (["a", "e", "i", "o", "u"].includes(word[0].toLowerCase())){
        console.log(word)
    }
}

// 7. Use reduce to console.log the longest word in an array of strings.

const stringArr = ["cat", 'dog', 'elephant', 'hippopotamus', 'zebra']

const longestWord = atringArr.reduce((longest, word) => {
    return word.length > longest.length ? word : longest 
}, "")
console.log(longestWord)

// 8. Use map to add the string "!" at the end of each word in an array and console.log the new array.

const wordArr = ["hello", "world", "JavaScript", "is", "fun"]

const excitedWords = wordArr.map(word => word + "!")
console.log(excitedWords)

// 9. Use filter to remove all numbers less than 10 from an array and console.log the result.

const numArray = [5, 12, 8, 20, 3, 15, 7]

const filteredNumbers = numArray.filter(num => num >= 10)
console.log(filteredNumbers)

// 10. Use a for loop to calculate the sum of numbers from 1 to 50 and console.log the sum.

let sum = 0
for ( let i = 1; i <=50; i++){
    sum += i
    console.log(sum)
}
