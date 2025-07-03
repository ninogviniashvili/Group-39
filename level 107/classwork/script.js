let list = document.getElementById("list");
let name = ["hello", "hi", "hey"];

for (let i = 0; i < name.length; i++) {
    let item = document.createElement("li");
    let text = document.createTextNode(name[i] + i);
    item.appendChild(text);
    list.appendChild(item);
}