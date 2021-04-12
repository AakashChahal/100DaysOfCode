"use strict";

// Variables
let contOp = 0;
const outputEl = document.getElementById("output");
let output = Number(outputEl.textContent);
const clearOutput = document.getElementById("clear");
const backspace = document.getElementById("del");

// Functions
const evalExpression = function () {
    console.log(output);
    console.log(output+);
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
        const operator = e.target.textContent;
        const val = outputEl.textContent;
        evalExpression(operator);
        outputEl.textContent += ` ${operator} `;
    }
};

// Events
document.querySelectorAll(".num").forEach((numEl) => {
    numEl.addEventListener("click", showNumOnScreen);
});

document.querySelectorAll(".op").forEach((opEl) => {
    opEl.addEventListener("click", getOperator);
});

document;
