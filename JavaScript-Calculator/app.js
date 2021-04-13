"use strict";

// Variables
// let contOp = 0;
// let operator = "";
const outputEl = document.getElementById("output");
let output = 0;
let val1 = 0;
let val2 = 0;
let operator = "";
const clearOutput = document.getElementById("clear");
const backspace = document.getElementById("del");

// Functions
const evalExpression = function (e) {
    val2 = Number(outputEl.textContent);
    console.log(val1, val2, operator);
    switch (operator) {
        case "+":
            output = val1 + val2;
            console.log(output);
            break;
        case "-":
            output = val1 - val2;
            console.log(output);
            break;
        case "×":
            output = val1 * val2;
            console.log(output);
            break;
        case "÷":
            output = val1 / val2;
            console.log(output);
            break;

        default:
            break;
    }
    outputEl.textContent = output;
};

const showNumOnScreen = function (e) {
    const n = e.target.textContent;
    // contOp = 0;
    outputEl.textContent == 0
        ? (outputEl.textContent = n)
        : (outputEl.textContent += n);
};

const getOperator = function (e) {
    // contOp++;
    val1 = Number(outputEl.textContent);
    operator = e.target.textContent;
    outputEl.textContent = "";
};

// Events
document.querySelectorAll(".num").forEach((numEl) => {
    numEl.addEventListener("click", showNumOnScreen);
});

document.querySelectorAll(".op").forEach((opEl) => {
    opEl.addEventListener("click", getOperator);
});

document.getElementById("eq").addEventListener("click", evalExpression);

clearOutput.addEventListener("click", function () {
    outputEl.textContent = "";
    val2 = 0;
    val1 = 0;
    output = 0;
});

backspace.addEventListener("click", function () {
    console.log(typeof outputEl.textContent);
    outputEl.textContent = outputEl.textContent.slice(
        outputEl.textContent.length - 1,
        1
    );
});
