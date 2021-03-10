let form = document.getElementById("addForm");
let itemList = document.getElementById("items");
let filter = document.getElementById("filter");

form.addEventListener("submit", addItem);

itemList.addEventListener('click', removeItem);

filter.addEventListener('keyup', filterItems);

function addItem(e) {
  e.preventDefault();

  // taking new input
  let newItem = document.getElementById("item");

  // creating new element
  let li = document.createElement("li");
  li.className = "list-group-item";
  // add text node with input value
  li.appendChild(document.createTextNode(newItem.value));
  newItem.value = "";

  // creating delete button for new element
  let deleteBtn = document.createElement('button');
  deleteBtn.classList = 'btn btn-danger btn-sm float-right delete';

  // append text node
  deleteBtn.appendChild(document.createTextNode('X'));

  // append dele button to new list item
  li.appendChild(deleteBtn);

  itemList.appendChild(li);
}

function removeItem(e) {
  if (e.target.classList.contains('delete')) {
    if(confirm("Are you sure?")) {
      let li = e.target.parentElement;
      itemList.removeChild(li);
    }
  }
}

function filterItems(e) {
  let text = e.target.value.toLowerCase().replace(' ', '');
  console.log(text);

  // get list elements
  let items = itemList.getElementsByTagName('li');

  // convert to array
  Array.from(items).forEach(function(item) {
    let itemName = item.firstChild.textContent.replace(' ', '');
    if (itemName.toLowerCase().indexOf(text) != -1) {
      item.style.display = "block";
    }
    else {
      item.style.display = "none";
    }
  });
}
