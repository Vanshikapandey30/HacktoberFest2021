const billAmount = document.querySelector("#bill-amount");
const nextButton = document.querySelector("#next-btn");
const mainMessage = document.querySelector("#main-message");
const revealPart = document.querySelector("#reveal-div");
const cashGiven = document.querySelector("#cash-given");
const checkButton = document.querySelector("#check-amount")
const message = document.querySelector("#error-message");
const changeTable = document.querySelector("#change-table");
const noteArray = [2000, 500, 100, 20, 10, 5, 1];
const numberOfNotes = document.querySelectorAll(".no-of-notes");

revealPart.style.display = "none";

nextButton.addEventListener("click", () => {

    if (billAmount.value) {
        if (Number(billAmount.value) > 0) {
            revealPart.style.display = "block";
            mainMessage.style.display = "none";
            nextButton.style.display = "none";

        } else {
            firstMessage("That should be a valid number");
        }
    } else {
        firstMessage("Sorry! you should enter a value");
    }

})

checkButton.addEventListener("click", () => {
    message.style.display = "none";

    const cashValue = Number(cashGiven.value);
    const billValue = Number(billAmount.value);
    if (billAmount.value && cashGiven.value) {

        if (billValue > 0 && cashValue > 0) {

            if (cashValue >= billValue) {
                if (cashValue == billValue) {
                    messageShown("No change needed");
                changeTable.style.display = "none";

                } else {
                    changeTable.style.display = "block";
                    const payBackAmount = cashValue - billValue;
                    calculateChange(payBackAmount);

                }

            } else {
                messageShown("cash should be atleast equal to the bill amount");
                changeTable.style.display = "none";
            }
        } else {
            messageShown("Please enter valid values in the fields given");
            changeTable.style.display = "none";
        }

    } else {
        messageShown("Enter a valid amount!");
        changeTable.style.display = "none";
    }
});

function calculateChange(payBackAmount) {
    for (let i = 0; i < noteArray.length; i++) {
        const noteNumber = Math.trunc(payBackAmount / noteArray[i]);
        payBackAmount = payBackAmount % noteArray[i]; //updating the paybackamount value after one iteration
        numberOfNotes[i].innerText = noteNumber; // updating the noofnotes box from the first divides and truncated value
    }
}


function messageShown(result) {
    message.style.display = "block";
    message.innerText = result;
}

function firstMessage(main) {
    mainMessage.style.display = "block";
    mainMessage.innerText = main;
}