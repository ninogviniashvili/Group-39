const header = document.querySelector('h1')
const form = document.querySelector('form')
const username = form.username
const password = form.password
const button = form.querySelector('button')


const user = localStorage.getItem('username')
const pass = localStorage.getItem('password')

if  (user !== "" && pass !== "") {
    header.textContent = `welcome ${user}`
    form.style.display = 'none'
}


console.dir(header)

function Handleform(e){
    e.preventDefault()
    const user = username.value
    const pass = password.value

    localStorage.setItem('username', user)
    localStorage.setItem('password', pass)

    form.style.display = 'none'
    header.textContent = `welcome ${user}`

}

form.addEventListener('submit', Handleform)