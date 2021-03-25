const dt = new Date();
const date = dt.getDate();
const month = dt.getMonth();
const year = dt.getFullYear();
const day = dt.getDay();
let currHr = new Date().getHours();
let currMin = new Date().getMinutes();
let currSec = new Date().getSeconds();
let count = 0;

const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "December",
    "November",
    "December",
];

const days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
];

document.getElementById("date").textContent +=
    date + " " + months[month] + " " + year + ", " + days[day];
setInterval(function () {
    currSec = new Date().getSeconds();
    currSec < 10
        ? (document.getElementById("sec").textContent = "0" + currSec)
        : (document.getElementById("sec").textContent = currSec);

    currMin = new Date().getMinutes();
    currMin < 10
        ? (document.getElementById("min").textContent = "0" + currMin)
        : (document.getElementById("min").textContent = currMin);

    currHr = new Date().getHours();
    currHr < 10
        ? (document.getElementById("hr").textContent = "0" + currHr)
        : (document.getElementById("hr").textContent = currHr);
}, 1000);
