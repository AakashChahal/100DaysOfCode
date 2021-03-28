const dt = new Date();

const date = dt.getDate();
const month = dt.getMonth();
const year = dt.getFullYear();
const day = dt.getDay();

let currHr;
let currMin;
let currSec;

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
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
];

document.getElementById("d").textContent +=
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
    if (currHr < 12) {
        if (currHr < 10) {
            document.getElementById("hr").textContent = "0" + currHr;
        }
        document.getElementById("AmPm").textContent = "AM";
    } else {
        currHr -= 12;
        if (currHr < 10) {
            document.getElementById("hr").textContent = "0" + currHr;
        }
        document.getElementById("AmPm").textContent = "PM";
    }
}, 1000);
