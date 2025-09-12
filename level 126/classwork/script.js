// JavaScript-ს აქვს ორი მეხსიერება Stack და Heap

// Stack = ინახება პრიმიტული ტიპები number, string, boolean...

// Heap = ინახება კომპლექსური ტიპები

// პრიმიტული = პირდაპირი მნიშვნელობა

// კომპლექსური = reference მისამართი Heap-ში, ცვლადი მხოლოდ მისამართს ინახავს

    const form = document.getElementById("passwordForm");
    const Input = document.getElementById("password");
    const message = document.getElementById("message");

    form.addEventListener("submit", function(event) {
      event.preventDefault();
      const password = Input.value;

      if (password.length >= 8) {
        message.textContent = "Valid Password!";
        message.className = "valid";
      } else {
        message.textContent = "Password must contain at least 8 characters!";
        message.className = "invalid";
      }
    });


    function manualIndexOf(ar, elM) {
  for (let i = 0; i < ar.length; i++) {
    if (ar[i] === elM) {
      return i; 
    }
  }
  return -1;
}


console.log(manualIndexOf([10, 20, 30, 40], 30)); 