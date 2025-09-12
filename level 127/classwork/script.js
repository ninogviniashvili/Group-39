const products = [
  { id: 1, name: "Cake", price: 15 },
  { id: 2, name: "ice cream", price: 5 },
  { id: 3, name: "cold tea", price: 7 }
]

const productsContainer = document.getElementById("products")
const cartItems = document.getElementById("cart-items")

for (let product of products) {
  const productDiv = document.createElement("div")
  productDiv.className = "product"

  const productName = document.createElement("h3")
  productName.textContent = product.name
  productDiv.appendChild(productName)

  const productPrice = document.createElement("p")
  productPrice.textContent = "Price: $" + product.price
  productDiv.appendChild(productPrice)

  const button = document.createElement("button")
  button.textContent = "Add to Cart"

  button.addEventListener("click", function() {
    const li = document.createElement("li")
    li.textContent = product.name + " - $" + product.price
    cartItems.appendChild(li)
  })

  productDiv.appendChild(button)
  productsContainer.appendChild(productDiv)
}




async function getData() {
  try {
    let response = await fetch("https://jsonplaceholder.typicode.com/posts");
    let data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error.message);
  }
}

getData();



// promise-ს JavaScript-ში - რომელიც წარმოადგენს ასინქრონული ოპერაციის შედეგს.
// მას აქვს სამი მდგომარეობა:

// pending (მოლოდინი) – ოპერაცია ჯერ არ დასრულებულა.

// fulfilled (შესრულებული) – ოპერაცია წარმატებით დასრულდა და დაბრუნდა შედეგი.

// rejected (უარყოფილი) – ოპერაცია ჩავარდა და დააბრუნა შეცდომა.

// მაგალითად დავრეკე მეგობართან და ვუთხარი რომ დამირეკოს. როცა დამირეკავს, ეს იქნება resolve, თუ ვერ დამირეკავს  reject

// ასინქრონიზაცია სარეცხის მანქანაში ჩავდე სარეცხი. მანამ სანამ რეცხავს, მე ვაგრძელებ სხვა საქმეებს. როცა რეცხვა დასრულდება, მაფრთხილებს ხმით.