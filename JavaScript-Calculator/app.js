"use strict";

// VARIABLES
const inputNumber = document.getElementById("numbers");
const operator = document.getElementById("operator");
const tempOutput = document.getElementById("tempOut");
const output = document.getElementById("output");
const numpad = document.querySelectorAll(".num");
const allOperators = document.querySelectorAll(".op");
const equal = document.getElementById("eq");

// FUNCTIONS
const getNumberFromNumpad = (e) => {
    inputNumber.textContent === "0"
        ? (inputNumber.textContent = e.target.textContent)
        : (inputNumber.textContent += e.target.textContent);
};

// EVENTS
numpad.forEach((num) => {
    num.addEventListener("click", getNumberFromNumpad);
});
