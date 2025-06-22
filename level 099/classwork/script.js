function addButton() {
    let container = document.getElementById('button-container');

    let newButton = document.createElement('button');

    newButton.textContent = 'Click Me!';

    container.appendChild(newButton);
}
