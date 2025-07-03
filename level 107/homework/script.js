// 1. შექმენით ფუნქცია, რომელიც იღებს რიცხვების მასივს და თითოეულ რიცხვს ბეჭდავს for ციკლის გამოყენებით.
// 2. შექმენით სახელების მასივი, შემდეგ, გამოიყენეთ for ციკლი თითოეული სახელის და მისი პოზიციის დასაბეჭდად.
// 3. შექმენით პროგრამა, რომელიც მასივში თითოეულ რიცხვს ამრავლებს 2-ზე და შედეგს ბეჭდავს მათ for ციკლის გამოყენებით.
// 4. დაწერეთ ფუნქცია, რომელიც for ციკლის გამოყენებით ითვლის მასივში რამდენი ელემენტია 10-ზე მეტი.
// 5. გამოიყენეთ for ციკლი მასივის ყველა ელემენტის შესაჯამებლად და საბოლოო შედეგის დასაბეჭდად.


// 1. შექმენით ფუნქცია, რომელიც იღებს რიცხვების მასივს და თითოეულ რიცხვს ბეჭდავს for ციკლის გამოყენებით.

function printNumbers(numbers) {
    for (let i = 0; i < numbers.length; i++) {
        console.log(numbers[i]);
    }
}

// 2. შექმენით სახელების მასივი, შემდეგ, გამოიყენეთ for ციკლი თითოეული სახელის და მისი პოზიციის დასაბეჭდად.

function printNamesWithIndex(names) {
    for (let i = 0; i < names.length; i++) {
        console.log(`Name: ${names[i]}, Index: ${i}`);
    }
}

// 3. შექმენით პროგრამა, რომელიც მასივში თითოეულ რიცხვს ამრავლებს 2-ზე და შედეგს ბეჭდავს მათ for ციკლის გამოყენებით.

function multiplyNumbersByTwo(numbers) {
    for (let i = 0; i < numbers.length; i++) {
        console.log(numbers[i] * 2);
    }
}

// 4. დაწერეთ ფუნქცია, რომელიც for ციკლის გამოყენებით ითვლის მასივში რამდენი ელემენტია 10-ზე მეტი.

function countElementsGreaterThanTen(numbers) {
    let count = 0;
    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] > 10) {
            count++;
        }
    }
    return count;
}

// 5. გამოიყენეთ for ციკლი მასივის ყველა ელემენტის შესაჯამებლად და საბოლოო შედეგის დასაბეჭდად.

function sumArrayElements(numbers) {
    let sum = 0;
    for (let i = 0; i < numbers.length; i++) {
        sum += numbers[i];
    }
    console.log(sum);
}


document.querySelector