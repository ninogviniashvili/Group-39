function calculatePrice() {
    const ageValue = document.getElementById("ageInput").value;
    const age = parseInt(ageValue);
    const result = document.getElementById("result");

    let price;
    if (age < 6) {
      price = "the ticket is free.";
    } else if (age >= 6 && age <= 17) {
      price = "ticket price is 5 GEL";
    } else if (age >= 18 && age <= 64) {
      price = "ticket price is 10 GEL ";
    } else if (age >= 65) {
      price = "ticket price is 7 GEL.";
    }

    result.textContent = price;
    result.style.color = "#00ffc8";
  }