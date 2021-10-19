let userScore = 0;
let compScore = 0;
const userScoreSpan = document.getElementById("user-score");
const conmpScoreSpan = document.getElementById("comp-score");
const scoreBoardDiv = document.querySelector(".score-board");
const resultDiv = document.querySelector(".result >p");
const rockDiv = document.getElementById("r");
const paperDiv = document.getElementById("p");
const scissorsDiv = document.getElementById("s");

function getCompChoice(){
  const choices = ["r","p","s"];
  const randomNumber = (Math.floor(Math.random()*3));
  return choices[randomNumber];
}

function convert(letter){
  if(letter=="r") return "Rock";
  if(letter=="p") return "Paper";
  if(letter=="s") return "Scissors";
}

function win(userChoice,compChoice){
  userScore++;
  userScoreSpan.innerHTML = userScore;
  conmpScoreSpan.innerHTML = compScore;
  let subUserWord = "User".fontsize(3).sub();
  let subCompWord = "Comp".fontsize(3).sub();
  resultDiv.innerHTML = `${convert(userChoice)}${subUserWord} beats ${convert(compChoice)}${subCompWord}. You win!`;
  document.getElementById(userChoice).classList.add("green-glow");
  setTimeout(function(){ document.getElementById(userChoice).classList.remove("green-glow") },200);
}

function lose(userChoice,compChoice){
  compScore++;
  userScoreSpan.innerHTML = userScore;
  conmpScoreSpan.innerHTML = compScore;
  let subUserWord = "User".fontsize(3).sub();
  let subCompWord = "Comp".fontsize(3).sub();
  resultDiv.innerHTML = `${convert(userChoice)}${subUserWord} loses to ${convert(compChoice)}${subCompWord}. You lose!`;
  document.getElementById(userChoice).classList.add("red-glow");
  setTimeout(function(){ document.getElementById(userChoice).classList.remove("red-glow") },200);
}

function draw(userChoice,compChoice){
  userScoreSpan.innerHTML = userScore;
  conmpScoreSpan.innerHTML = compScore;
  let subUserWord = "User".fontsize(3).sub();
  let subCompWord = "Comp".fontsize(3).sub();
  resultDiv.innerHTML = `${convert(userChoice)}${subUserWord} is equal to ${convert(compChoice)}${subCompWord}. It's a draw!`;
  document.getElementById(userChoice).classList.add("grey-glow");
  setTimeout(function(){ document.getElementById(userChoice).classList.remove("grey-glow") },200);
}

function game(userChoice){
  const compChoice = getCompChoice();
  switch (userChoice + compChoice) {
    case "pr":
    case "rs":
    case "sp":
    win(userChoice,compChoice);
    break;
    case "rp":
    case "sr":
    case "ps":
    lose(userChoice,compChoice);
    break;
    case "pr":
    case "rs":
    case "sp":
    draw(userChoice,compChoice);
    break;
  }
}

function main(){
  rockDiv.addEventListener("click",function(){
    game("r");
  });
  paperDiv.addEventListener("click",function(){
    game("p");
  });
  scissorsDiv.addEventListener("click",function(){
    game("s");
  });
}

main();
