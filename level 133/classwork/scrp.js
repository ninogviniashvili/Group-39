// 1.
const number = [1,2,3,4,5]
const double = number.map(num => num*2)
console.log(double)

// 2. 
const ords = ['piano', 'book', 'movie', ]
const upper = ords.map(word=> word.toUpperCase())
console.log(upper)

// 3. 
const num2 = [10, 20, 30]
const newL = []
const plusFive = num2.map(num => {
const val = num + 5
newL.push(val)
return val
})
console.log("newList:", newL)

// 4

const num3 = [2, 4, 6, 8]
const square = num3.map(num => num ** 2)
console.log(square)

// 5

const namess = ['nino', 'mari', 'aabfja']
const greet = namess.map(name=> 'Hello, ${name}!')