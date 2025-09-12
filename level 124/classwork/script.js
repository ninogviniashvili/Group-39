    const form = document.getElementById("loginForm");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      const email = emailInput.value.trim();
      const password = passwordInput.value;

      console.log("enter email:", email);
      console.log("enter password", password);

    });