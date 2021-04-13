"use strict";

// Variables
let contOp = 0;
let operator = "";
const outputEl = document.getElementById("output");
let output = 0;
const clearOutput = document.getElementById("clear");
const backspace = document.getElementById("del");

// Functions
const evalExpression = function () {
    switch (operator) {
        case "+":
            output += Number(outputEl.textContent);
            console.log(output);
            break;
        case "-":
            output -= Number(outputEl.textContent);
            console.log(output);
            break;
        case "×":
            output *= Number(outputEl.textContent);
            console.log(output);
            break;
        case "÷":
            output /= Number(outputEl.textContent);
            console.log(output);
            break;

        default:
            break;
    }
};

const showNumOnScreen = function (e) {
    const n = e.target.textContent;
    contOp = 0;
    outputEl.textContent == 0
        ? (outputEl.textContent = n)
        : (outputEl.textContent += n);
};

const getOperator = function (e) {
    contOp++;
    if (contOp === 1) {
        operator = e.target.textContent;
        const n = Number(outputEl.textContent);
        switch (operator) {
            case "+":
                output += n;
                console.log(output);
                break;
            case "-":
                output -= n;
                console.log(output);
                break;
            case "×":
                output *= n;
                console.log(output);
                break;
            case "÷":
                output /= n;
                console.log(output);
                break;

            default:
                break;
        }
        outputEl.textContent = "";
    }
};

// Events
document.querySelectorAll(".num").forEach((numEl) => {
    numEl.addEventListener("click", showNumOnScreen);
});

document.querySelectorAll(".op").forEach((opEl) => {
    opEl.addEventListener("click", getOperator);
});

document.getElementById("eq").addEventListener("click", function () {
    switch (operator) {
        case "+":
            output += Number(outputEl.textContent);
            console.log(output);
            break;
        case "-":
            output -= Number(outputEl.textContent);
            console.log(output);
            break;
        case "×":
            output *= Number(outputEl.textContent);
            console.log(output);
            break;
        case "÷":
            output /= Number(outputEl.textContent);
            console.log(output);
            break;

        default:
            break;
    }
});
