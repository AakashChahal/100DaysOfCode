"use strict";

// VARIABLES
let currNumber = "";
let currAns = 0;
let currOp = "";
let countOperator = 0;
const inputNumber = document.getElementById("numbers");
const tempOutput = document.getElementById("tempOut");
const numpad = document.querySelectorAll(".num");
const allOperators = document.querySelectorAll(".op");
const equal = document.getElementById("eq");
const audio = document.getElementById("sound");

// FUNCTIONS
const getNumberFromNumpad = (e) => {
    audio.currentTime = 0;
    audio.play();
    if (tempOutput.textContent.includes("=")) {
        tempOutput.textContent = "";
        inputNumber.textContent = e.target.textContent;
        countOperator = 0;
        currAns = 0;
    } else {
        inputNumber.textContent === "0" || inputNumber.textContent === ""
            ? (inputNumber.textContent = e.target.textContent)
            : (inputNumber.textContent += e.target.textContent);
    }
};

const calcAnswer = function () {
    switch (tempOutput.textContent.slice(-1)) {
        case "+":
            if (currAns == 0) {
                currAns =
                    Number(
                        tempOutput.textContent.slice(
                            0,
                            tempOutput.textContent.indexOf(" ")
                        )
                    ) + currNumber;
            } else {
                currAns += currNumber;
            }
            break;
        case "-":
            if (currAns == 0) {
                currAns =
                    Number(
                        tempOutput.textContent.slice(
                            0,
                            tempOutput.textContent.indexOf(" ")
                        )
                    ) - currNumber;
            } else {
                currAns -= currNumber;
            }
            break;
        case "×":
            if (currAns == 0) {
                currAns =
                    Number(
                        tempOutput.textContent.slice(
                            0,
                            tempOutput.textContent.indexOf(" ")
                        )
                    ) * currNumber;
            } else {
                currAns *= currNumber;
            }
            break;
        case "÷":
            if (currAns == 0) {
                currAns =
                    Number(
                        tempOutput.textContent.slice(
                            0,
                            tempOutput.textContent.indexOf(" ")
                        )
                    ) / currNumber;
            } else {
                currAns /= currNumber;
            }
            break;

        default:
            break;
    }
};

const currentOperator = (e) => {
    audio.currentTime = 0;
    audio.play();
    countOperator += 1;
    currNumber = Number(inputNumber.textContent);
    currOp = e.target.textContent;
    if (countOperator <= 1) tempOutput.textContent = `${currNumber} ${currOp}`;
    else {
        calcAnswer();
        tempOutput.textContent = `${currAns} ${currOp}`;
    }
    inputNumber.textContent = "";
};

// EVENTS
numpad.forEach((num) => {
    num.addEventListener("click", getNumberFromNumpad);
});

allOperators.forEach((op) => {
    op.addEventListener("click", currentOperator);
});

equal.addEventListener("click", function () {
    audio.currentTime = 0;
    audio.play();
    currNumber = Number(inputNumber.textContent);
    calcAnswer();
    tempOutput.textContent += " " + currNumber + " =";
    inputNumber.textContent = currAns;
});

document.getElementById("clear").addEventListener("click", function () {
    audio.currentTime = 0;
    audio.play();
    inputNumber.textContent = "0";
    tempOutput.textContent = "0";
    currAns = 0;
    countOperator = 0;
});

document.getElementById("del").addEventListener("click", function () {
    audio.currentTime = 0;
    audio.play();
    inputNumber.textContent = inputNumber.textContent.slice(0, -1);
    if (inputNumber.textContent === "") {
        inputNumber.textContent = "0";
    }
});
