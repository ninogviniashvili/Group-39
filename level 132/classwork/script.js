// 1. დააგენერირეთ random ციფრი 1-იდან 100-მდე და გამოიტანეთ კონსოლში (random)
let rand= Math.random()*100
    console.log(rand)
// 2. გამოიყენეთ რამდენიმე რიცხვზე floor() ფუნქცია და დააკვირდით რას აკეთებს.
console.log(Math.floor(3))
console.log(Math.floor(2))
console.log(Math.floor(1.5))
// 3. დაწერეთ პირობა ჩვეულებრივი conditional-ის გამოყენებით, შემდეგ კი შეამოკლეთ და მიუწერეთ ქვევით მისი ternary ვარიანტი
let a=8
if (a > 5) {
    console.log("8 is bigger than 5")
} else {
    console.log("8 is smaller to 5")
}
a > 5 ? console.log("8 is bigger than 5") : console.log("8 is smaller 5");
// 4. შექმენით რიცხვების სია და გამოიყენეთ მასზე შემდეგი ფუნქციები: push, pop, shift, unshift, slice.
let nums = [1,2,3,4,5]
nums.push(6)
console.log(nums)
nums.pop()
console.log(nums)
nums.shift()
console.log(nums)
nums.unshift(0)
console.log(nums)
nums.slice(1, 4)
console.log(nums)
// 5. შექმენით ელემენტების სია, რომელსაც გადაუვლით map()-ით და გააორმაგებთ თითოეულ ელემენტს.
let numbs=[1,2,3,4,5]
let numbs2=numbs.map(function(number) {
    return number*2
})
console.log(numbs2)
// 6. შექმენით სტრინგების სია, რომელსაც გადაუვლით map()-ით და თთოეულ ელემენტს გვერდზე მიუწერთ თავის ინდექსს.
let fruits = ["Apple", "Banana", "Banana","Cherry"];
let strings=fruits.map(function(fruit, index) {
    return fruit + ":" + index
})
console.log(strings)
// 7. შექმენით ელემენტების სია, გადაუარეთ map-ით და შეკრიბეთ ყველა ელემენტი, ბოლოს დააბრუნეთ ჯამი
let numbes=[1,2,3,4,5]
let sum=0
let nu=numbes.map(function(numbers) {
    return sum + numbes
})

console.log(sum)
