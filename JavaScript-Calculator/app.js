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

// FUNCTIONS
const getNumberFromNumpad = (e) => {
    if (Number(tempOutput)) {
        inputNumber.textContent = e.target.textContent;
    } else {
        inputNumber.textContent === "0" || inputNumber.textContent === ""
            ? (inputNumber.textContent = e.target.textContent)
            : (inputNumber.textContent += e.target.textContent);
    }
};

const currentOperator = (e) => {
    countOperator += 1;
    currNumber = Number(inputNumber.textContent);
    currOp = e.target.textContent;
    if (countOperator <= 1) tempOutput.textContent = `${currNumber} ${currOp}`;
    else {
        switch (
            tempOutput.textContent.slice(tempOutput.textContent.indexOf(-2, -1))
        ) {
            case "+":
                if (currAns == 0) {
                    currAns =
                        currNumber +
                        Number(
                            tempOutput.textContent.slice(
                                0,
                                tempOutput.textContent.indexOf(" ")
                            )
                        );
                } else {
                    currAns += currNumber;
                }
                break;
            case "-":
                if (currAns == 0) {
                    currAns =
                        currNumber -
                        Number(
                            tempOutput.textContent.slice(
                                0,
                                tempOutput.textContent.indexOf(" ")
                            )
                        );
                } else {
                    currAns -= currNumber;
                }
                break;
            case "×":
                if (currAns == 0) {
                    currAns =
                        currNumber *
                        Number(
                            tempOutput.textContent.slice(
                                0,
                                tempOutput.textContent.indexOf(" ")
                            )
                        );
                } else {
                    currAns *= currNumber;
                }
                break;
            case "÷":
                if (currAns == 0) {
                    currAns =
                        currNumber /
                        Number(
                            tempOutput.textContent.slice(
                                0,
                                tempOutput.textContent.indexOf(" ")
                            )
                        );
                } else {
                    currAns /= currNumber;
                }
                break;

            default:
                break;
        }
        tempOutput.textContent = `${currAns} ${currOp}`;
    }
    inputNumber.textContent = "";
};

const showAnswer = () => {
    currentOperator();
    inputNumber.textContent = currAns;
};

// EVENTS
numpad.forEach((num) => {
    num.addEventListener("click", getNumberFromNumpad);
});

allOperators.forEach((op) => {
    op.addEventListener("click", currentOperator);
});

equal.addEventListener("click", showAnswer);

document.getElementById("clear").addEventListener("click", function () {
    inputNumber.textContent = "0";
    tempOutput.textContent = "0";
    currAns = 0;
    countOperator = 0;
});

document.getElementById("del").addEventListener("click", function () {
    inputNumber.textContent = inputNumber.textContent.slice(0, -1);
    if (inputNumber.textContent === "") {
        inputNumber.textContent = "0";
    }
});
