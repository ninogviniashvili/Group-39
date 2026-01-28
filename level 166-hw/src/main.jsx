import {
  findA,
  findOlder,
  findLWord,
  findCheap,
  findTop,
  findNeg,
  findIng,
  findActivUs,
  findMultTen,
  findFiveLetFr,

  lastBig,
  getLastWE,
  getLastYU,
  getLastOdd,
  getLastVow,
  lastIndexOverFifty,
  lastIndStrtS,
  lastActiveUsInd,
  lastDivisibleByThree,
  lastFourLetWrdInd,
  findTwentyFive,
  findApple,
  findFirstAIndex,
  findCatIndex,
  findHundred
} from './App.jsx';

// 1
console.log(findA(["Banana", "Apple", "Avocado"]))

// 2
console.log(
  findOlder([
    { name: "Luka", age: 25 },
    { name: "Nino", age: 34 }
  ])
)

// 3
console.log(findLWord(["cat", "house", "elephant"]))

// 4
console.log(
  findCheap([
    { title: "Shoes", price: 50 },
    { title: "T-shirt", price: 15 }
  ])
)

// 5
console.log(
  findTop([
    { name: "Gio", grade: "B" },
    {name: "Ana", Grade: "A"}
  ])
)

// 6
console.log(findNeg([5, 8, -3, 10]))


// 7
console.log(findIng(["run", "jumping", "walk"]))


// 8
console.log(
  findActivUs([
    { name: "Ana", isActive: false },
    { name: "Saba", isActive: true }
  ])
)

// 9
console.log(findMultTen([3, 7, 20, 11]))

// 10
console.log(findFiveLetFr(["pear", "apple", "banana"]))

// 11
console.log(lastBig([20, 150, 80, 200]))

// 12
console.log(getLastWE(["sky", "tree", "blue", "sun"]))

// 13
console.log(getLastYU([
    { name: "Nika", age: 30 },
    { name: "Lia", age: 22 },
    { name: "Mose", age: 19 }
  ])
)


// 14
console.log(getLastOdd([2, 4, 7, 10, 9]))

// 15
console.log(getLastVow(["dog", "apple", "tree", "orange"]))

// 16
console.log(lastIndexOverFifty([10, 60, 30, 80]))

// 17
console.log(lastIndStrtS(["Sun", "Moon", "Star", "Sky"]))

// 18
console.log(
  lastActiveUsInd([
    { name: "Ana", isActive: true },
    { name: "Gio", isActive: false },
    { name: "Luka", isActive: true }
  ])
)

// 19
console.log(lastDivisibleByThree([4, 9, 10, 15]))

// 20
console.log(lastFourLetWrdInd(["tree", "rock", "mountain", "wind"]))

// 21
console.log(findTwentyFive([5, 25, 40]))

// 22
console.log(findApple(["banana", "apple", "pear"]))

// 23
console.log(findFirstAIndex(["b", "c", "a", "d"]))

// 24
console.log(findCatIndex(["dog", "cat", "bird"]))

// 25
console.log(findHundred([10, 50, 90]))
