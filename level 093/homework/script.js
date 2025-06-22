// 1

const book = {
    name: "The Great Gatsby",
    author: "F. Scott Fitzgerald",
    pages: 180,
    genre: "Fiction",
    isAvailable: true
};
console.log("Name:", book.name);
console.log("Author:", book.author);
console.log("Pages:", book.pages);
console.log("Genre:", book.genre);
console.log("Available:", book.isAvailable);

// 2

const student = {
    name: "Ana",
    grade: 85,
    passed: true,
    year: 2024
};

if (student.passed) {
    console.log("student passed the grade");
} else {
    console.log("student failed the grade");
}

// 3

const movie = {
    title: "Inception",
    rating: "PG-13",
    duration: 148, // in minutes
    yearReleased: 2010,
    isAnimated: false
};

console.log(`The movie ${movie.title} is rated ${movie.rating} and was released in ${movie.yearReleased}.`);

// 4

const phone = {
    brand: "iPhone",
    model: "iPhone 11",
    storage: "128GB",
    batteryLife: "24h",
    is5G: true
};

if (phone.is5G) {
    console.log("supports 5G");
} else {
    console.log("doesn't support 5G");
}

// 5

const game = {
    name: "Among Us",
    players: 4,
    online: true,
    releaseYear: 2018,
    genre: "Party"
};
if (game.players > 1) {
    console.log("Multiplayer game");
} else {
    console.log("Single player game");
}