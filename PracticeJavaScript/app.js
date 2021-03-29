// variables
const next = document.getElementById("next");
const prev = document.getElementById("prev");
const image = document.getElementById("my-img");
let imageNum = 0;

// functions
const showNextImage = function () {
    if (imageNum < 8) {
        imageNum++;
        image.src = `images/image${imageNum}.jpg`;
    } else {
        alert("You've reached the end");
    }
};

const showPrevImage = function () {
    if (imageNum > 0) {
        imageNum--;
        image.src = `images/image${imageNum}.jpg`;
    } else {
        alert("You've reached the end");
    }
};

// events
next.addEventListener("click", showNextImage);
prev.addEventListener("click", showPrevImage);
