const diceImages= ["dice1.png","dice2.png","dice3.png","dice4.png","dice5.png","dice6.png"];

const dice1Element=document.getElementById("dice1");
const dice2Element=document.getElementById("dice2");
const resultElement=document.getElementById("result");
const rollButton=document.getElementById("rollButton");

function rollDice() {
    return Math.floor(Math.random()*6)+ 1;
}

rollButton.addEventListener("click", () => {
    const dice1Value=rollDice();
    const dice2Value=rollDice();

    dice1Element.src=diceImages[dice1Value-1];
    dice2Element.src=diceImages[dice2Value-1];

    const sum=dice1Value+dice2Value;
    resultElement.textContent=sum.toString();
})

