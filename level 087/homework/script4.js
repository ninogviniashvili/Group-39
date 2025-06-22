//5

let randomNumber = 46; 
let guess = 0;

while (guess !== randomNumber) {
    guess = (prompt("Guess a number between 1 and 50:"));

    if (guess < randomNumber) {
        alert("your numbrr is too low. Try again!");
    } else if (guess > randomNumber) {
        alert("your number is too high. Try again!");
    } else if (guess = randomNumber) {
        alert("you guessed the correct number! ");
    } else {
        alert("enter a number.");
    }
}