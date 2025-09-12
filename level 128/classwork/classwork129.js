let Score = 0;
let computerScore = 0;

function playGame(userChoice) {
  const choices = ['rock', 'paper', 'scissors'];
  const computerChoice = choices[Math.floor(Math.random() * 3)];

  let resultText = '';
  if (userChoice === computerChoice) {
    resultText = 'TIE!';
  } else if (
    (userChoice === 'rock' && computerChoice === 'scissors') ||
    (userChoice === 'paper' && computerChoice === 'rock') ||
    (userChoice === 'scissors' && computerChoice === 'paper')
  ) {
    Score++;
    resultText = 'WIN!';
  } else {
    computerScore++;
    resultText = 'AI WON!';
  }

  document.getElementById('user-score').textContent = userScore;
  document.getElementById('computer-score').textContent = computerScore;
  document.getElementById('result').textContent = resultText;
  document.getElementById('status').textContent = 
    `CHOOSE: ${userChoice}, COMP: ${computerChoice}`;
}

// 2

const myFrm = document.querySelector('frm');
const myInpt = document.getElementById("myInpt");
const box = document.getElementById("box");

myFrm.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = myInpt.value;
    const getData = fetch(`https://api.github.com/users/${name}`);

    getData
        .then(res => res.json())
        .then(showDta)
        .catch(err => console.log("Error: " + err));
});

function showDta(info) {
    box.innerHTML = `
        <div>
            <h2>${info.name}</h2>
            <p>Company: ${info.company}</p>
            <p>${info.bio}</p>
            <p>Repos: ${info.public_repos}</p>
            <img src="${info.avatar_url}" width="150" alt="Avatar"/>
        </div>
    `;
}