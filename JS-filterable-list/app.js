// getting elements
let filterInput = document.getElementById("filterInput");
console.log(filterInput);
let ul = document.getElementById("names");
let listItems = ul.querySelectorAll("li.collection-item");
let listHeaders = ul.querySelectorAll("li.collection-header");

filterInput.addEventListener("click", searchInList);

function searchInList(e) {
    let inputValue = document.querySelector("#filterInput");
    inputValue.addEventListener("keyup", (e) => {
        let filterValue = document
            .getElementById("filterInput")
            .value.toLowerCase();
        // console.log(filterValue);
        for (let i = 0; i < listItems.length; i++) {
            let ch = listItems[i]
                .getElementsByTagName("a")[0]
                .innerText.toLowerCase();
            // console.log(ch);
            if (ch.indexOf(filterValue) > -1) {
                listItems[i].style.display = "";
            } else {
                listItems[i].style.display = "none";
            }
        }
    });
}

window.addEventListener("DOMContentLoaded", () => {
    for (let i = 0; i < listItems.length; i++) {
        listItems[i].classList.add("grey");
        listItems[i].classList.add("darken-4");
    }
    for (let i = 0; i < listHeaders.length; i++) {
        listHeaders[i].classList.add("accent-4");
        listHeaders[i].classList.add("grey");
    }
});
