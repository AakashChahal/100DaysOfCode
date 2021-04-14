"use strict";

// VARIABLES
let currNumber = "";
let currEval = 0;
const inputNumber = document.getElementById("numbers");
const operator = document.getElementById("operator");
const tempOutput = document.getElementById("tempOut");
const output = document.getElementById("answer");
const numpad = document.querySelectorAll(".num");
const allOperators = document.querySelectorAll(".op");
const equal = document.getElementById("eq");

// FUNCTIONS
const getNumberFromNumpad = (e) => {
    output.classList.add("hide");
    inputNumber.classList.remove("hide");
    inputNumber.textContent === "0"
        ? (inputNumber.textContent = e.target.textContent)
        : (inputNumber.textContent += e.target.textContent);
    currNumber = Number(inputNumber.textContent);
    // console.log(currNumber);
};

const currentOperator = (e) => {
    inputNumber.textContent = "";
    output.classList.add("hide");
    inputNumber.classList.add("hide");
    const currOp = e.target.textContent;
    operator.textContent = currOp;
    console.log(currNumber);
    if (currEval === 0) {
        currEval = currNumber;
    } else {
        switch (currOp) {
            case "+":
                currEval += Number(currNumber);
                break;
            case "-":
                currEval -= Number(currNumber);
                break;
            case "×":
                currEval *= Number(currNumber);
                break;
            case "÷":
                currEval /= Number(currNumber);
                break;

            default:
                break;
        }
    }
    tempOutput.textContent = currEval;
};

const showAnswer = () => {
    const currOp = operator.textContent;
    // operator.textContent = currOp;
    console.log(currNumber);
    switch (currOp) {
        case "+":
            currEval += Number(currNumber);
            break;
        case "-":
            currEval -= Number(currNumber);
            break;
        case "×":
            currEval *= Number(currNumber);
            break;
        case "÷":
            currEval /= Number(currNumber);
            break;

        default:
            break;
    }
    currNumber = "";
    operator.textContent = "";
    tempOutput.textContent = "";
    output.textContent = currEval;
    output.classList.remove("hide");
    inputNumber.classList.add("hide");
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
    operator.textContent = "";
    tempOutput.textContent = "";
    currEval = 0;
    output.textContent = "";
    output.classList.add("hide");
    console.log("done");
});

document.getElementById("del").addEventListener("click", function () {
    inputNumber.textContent = inputNumber.textContent.slice(0, -1);
    if (inputNumber.textContent === "") {
        inputNumber.textContent = "0";
    }
});
