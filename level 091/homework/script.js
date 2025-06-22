function calculateBMI() {
    
    let weight = document.getElementById('weight').value
    let height = document.getElementById('height').value
    let result = document.getElementById('bmi') 
    
    weight = parseFloat(weight)
    height = parseFloat(height)
    
    height = height / 100
    let bmi = weight / (height * height)

    
if (bmi < 18.5){
    alert('You are underweight');
} 
else if (bmi>=18.5 && bmi<24.9){
    alert('You have a normal weight');
} 
else if (bmi>= 25 && bmi<29.9){
    alert('You are overweight');
} 



}


