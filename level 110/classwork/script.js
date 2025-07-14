// 1
function changeBallColor() {
    const ball = document.getElementById('ball');
    const colors = ['red', 'blue', 'green', 'yellow', 'purple'];
   for(let i=0; i<colors.length; i++){
    ball.style.color = colors[i]
   }
}

setInterval(changeBallColor, 5000);

// 2


window.onload = function() {
    console.log(5);
}

// 3
const list = ["hi", "hello", "hey", "how are you", "gamarjoba"];
const div = document.getElementById("div");

for (let i = 0; i < list.length; i++) {
    const h1 = document.createElement("h1");
    h1.textContent = list[i];
    div.appendChild(h1);
}
