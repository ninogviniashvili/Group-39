// API-დან წამოიღეთ ინფორმაცია პირველი პროდუქტის შესახებ და მისი მნიშვნელობები დაამატეთ/გამოიყენეთ html-ში,


// 'https://fakestoreapi.com/products/1'

fetch('https://fakestoreapi.com/products')
    .then(resp => resp.json())
    .then(products => {
    const product = products[0]; 
    const productBox = document.getElementById('productBox');
    prodB.innerHTML = `
        <div>
        <h1>${product.title}</h1>
        <img src="${product.image}" width="150">
        <p>${product.description}</p>
        <p>Price: $${product.price}</p>
    </div>
    `;
});

