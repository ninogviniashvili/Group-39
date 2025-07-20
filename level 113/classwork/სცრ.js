  const lightBtn = document.getElementById('lightModeBtn');
  const darkBtn = document.getElementById('darkModeBtn');

  lightBtn.addEventListener('click', () => {
    document.documentElement.style.setProperty('--background-color', '#ffffff');
      });


    darkBtn.addEventListener('click', () => {
    document.documentElement.style.setProperty('--background-color', '#000000ff');
  })
