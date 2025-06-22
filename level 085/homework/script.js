let value = 0
function counter1(){
    value += 5 
    document.getElementById("value").textContent = value
}


function counter2(){
    value = 0
    document.getElementById("value").textContent = value
}
function counter3(){
    value -=5 
    document.getElementById("value").textContent = value
}