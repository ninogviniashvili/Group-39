import { useState } from 'react'

//1
function findA(words) {
  return words.find(w=> w.startsWith('A'))
}

//2
function findOlder(users){
  return users.find(u => u.age > 30)
}

//3
function findLWord(word) {
  return word.find(w => w.length > 4)
}

//4
function findCheap(items){
  return items.find(i => i.price < 200)
}


//5
function findTop(student) {
  return student.find( s => s.score > 90)
}

//6
function findNeg(nums){
  return nums.find(n=> n< 0)
}

//7
function findIng(wordss){
  return wordss.find(w=> w.endsWith('ing'))
}

//8
function findActivUs(users){
  return users.find(u => u.isActive === true)
}

//9
function findMultTen(nu){
  return nu.find(n => n% 10 === 0)
}

//10
function findFiveLetFr(fruits){
  return fruits.find(f => f.length === 5)
}

//11

function lastBig(arr){
  return arr.findLast(w => w.length >4)
}

//12
function getLastWE(wor){
  return wor.findLast(w => w.endsWith('e'))
}

//13
function getLastYU(list){
  return list.findLast(u => u.age < 25)
}

//14 
function getLastOdd(nu){
  return nu.findLast(n => n % 2 !== 0)
}

//15
function getLastVow(wrd){
  return wrd.findLast(w => ['a','e','i','o','u'].includes(w[0].toLowerCase()))
}

// 16
function lastIndexOverFifty(na) {
  return na.findLastIndex(n => n > 50)
}

// 17
function lastIndStrtS(wo) {
  return wo.findLastIndex(w => w.startsWith("S"))
}

// 18
function lastActiveUsInd(lst) {
  return lst.findLastIndex(u => u.isActive === true)
}

// 19
function lastDivisibleByThree(numberas) {
  return numberas.findLastIndex(n => n % 3 === 0)
}

// 20
function lastFourLetWrdInd(sit) {
  return sit.findLastIndex(w => w.length === 4)
}

// 21
function findTwentyFive(ric) {
  return ric.indexOf(25)
}

// 22
function findApple(fru) {
  return fru.indexOf("apple")
}

// 23
function findFirstAIndex(letterss) {
  return letterss.indexOf("a")
}

// 24
function findCatIndex(animale) {
  return animale.indexOf("cat")
}

// 25
function findHundred(numbe) {
  return numbe.indexOf(100)
}

// 26
function lastTen(numb) {
  return numb.lastIndexOf(10)
}

// 27
function lastAppleIndex(fruitses) {
  return fruitses.lastIndexOf("apple")
}

// 28
function lastAChar(chars) {
  return chars.lastIndexOf("a")
}

// 29
function lastDog(animalls) {
  return animalls.lastIndexOf("dog")
}

// 30
function lastZero(numse) {
  return numse.lastIndexOf(0)
}

// 31
function removeLastNum(numss) {
  return numss.pop()
}

// 32
function removeLastFr(fruts) {
  return fruts.pop()
}

// 33
function emptyArray(ar) {
  while (ar.length > 0) {
    ar.pop()
  }
  return ar
}

// 34
function removeLastUser(uses) {
  return uses.pop()
}

// 35
function popAndStore(arrr) {
  const removedItem = arrr.pop()
  return removedItem
}

// 36
function removeFirstTwo(arre) {
  arre.splice(0, 2)
  return arre
}

// 37
function insertOrangeAndGrape(array) {
  array.splice(2, 0, "orange", "grape")
  return array
}

// 38
function replaceWithMango(aar) {
  aar.splice(3, 1, "mango")
  return aar
}

// 39
function removeLastThree(are) {
  are.splice(-3)
  return are
}

// 40
function insertInMiddle(arva, value) {
  const middle = Math.floor(arva.length / 2)
  arva.splice(middle, 0, value)
  return arva
}

export {
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
};