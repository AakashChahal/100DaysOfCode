// selectors
const todoInput = document.querySelector(".todo-input");
const todoButton = document.querySelector(".todo-button");
const todoList = document.querySelector(".todo-list");
const filterOption = document.querySelector('.filter-todo')

// event listeners
document.addEventListener('DOMContentLoaded', getTodos);
todoButton.addEventListener('click', addTodo);
todoList.addEventListener('click', deleteCheck);
filterOption.addEventListener('click', filterTodo);

// functions
function addTodo(e) {
    // prevent form from submitting
    e.preventDefault();
    // create todo div
    const todoDiv = document.createElement('div');
    todoDiv.classList.add('todo');
    const newTodo = document.createElement('li');
    newTodo.innerText = todoInput.value;
    newTodo.classList.add('todo-item');
    todoDiv.appendChild(newTodo);
    
    const checkBtn = document.createElement('button');
    checkBtn.innerHTML = '<i class="fas fa-check"></i>';
    checkBtn.classList.add("complete-btn");
    todoDiv.appendChild(checkBtn);
    
    const deleteBtn = document.createElement('button');
    deleteBtn.innerHTML = '<i class="fas fa-trash"></i>';
    deleteBtn.classList.add("delete-btn");
    todoDiv.appendChild(deleteBtn);

    todoList.appendChild(todoDiv);
    storeTodo(todoInput.value);
    todoInput.value = "";
};

function deleteCheck(e) {
    // deleting items
    if (e.target.classList.contains("delete-btn")) {
        const item = e.target;
        item.parentElement.classList.add("fall");
        // e.target.parentElement.remove();
        removeLocalTodos(item.parentElement);
        item.parentElement.addEventListener('transitionend', function() {
            item.parentElement.remove();
        })
    }

    // checking completed items
    if (e.target.classList.contains("complete-btn")) {
        e.target.parentElement.classList.toggle("completed");
        // console.log(e.target.parentElement);
    }

}

function filterTodo(e) {
    const todos = todoList.childNodes;
    todos.forEach(function(todo) {
        switch(e.target.value) {
            case 'all':
                todo.style.display = "flex";
                break;
            case 'completed':
                if(todo.classList.contains("completed")) {
                    todo.style.display = "flex";
                }
                else {
                    todo.style.display = "none";
                }
                break;
            
            case "uncompleted":
                if(todo.classList.contains("completed")) {
                    todo.style.display = "none";
                }
                else {
                    todo.style.display = "flex";
                }
                break;
        }
    });
}

function storeTodo(todo) {
    let todos;
    if (localStorage.getItem('todos') === null) todos = [];
    else todos = JSON.parse(localStorage.getItem('todos'));
    todos.push(todo);

    localStorage.setItem("todos", JSON.stringify(todos));
}

function getTodos() {
    let todos;
    if (localStorage.getItem('todos') === null) todos = [];
    else todos = JSON.parse(localStorage.getItem('todos'));
    todos.forEach(function(todo) {
        const todoDiv = document.createElement('div');
        todoDiv.classList.add('todo');

        const newTodo = document.createElement('li');
        newTodo.innerText = todo;
        newTodo.classList.add('todo-item');
        todoDiv.appendChild(newTodo);
        
        const checkBtn = document.createElement('button');
        checkBtn.innerHTML = '<i class="fas fa-check"></i>';
        checkBtn.classList.add("complete-btn");
        todoDiv.appendChild(checkBtn);
        
        const deleteBtn = document.createElement('button');
        deleteBtn.innerHTML = '<i class="fas fa-trash"></i>';
        deleteBtn.classList.add("delete-btn");
        todoDiv.appendChild(deleteBtn);

        todoList.appendChild(todoDiv);
    });
}

function removeLocalTodos(todo) {
    let todos;
    if (localStorage.getItem('todos') === null) todos = [];
    else todos = JSON.parse(localStorage.getItem('todos'));
    const todoIndex = todos.indexOf(todo.children[0].innerText);
    todos.splice(todoIndex, 1);
    localStorage.setItem("todos", JSON.stringify(todos));
}