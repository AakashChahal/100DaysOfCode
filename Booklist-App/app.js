// Book Class: Represents a book
class Book {
    constructor(title, author, isbn) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
    }
}

// UI class: Handles UI task
class UI {
    static displayBooks() {
        const books = Store.getBooks();
        books.forEach(book => UI.addBookToList(book));
    }

    static addBookToList(book) {
        const list = document.getElementById("book-list");
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${book.title}</td>
            <td>${book.author}</td>
            <td>${book.isbn}</td>
            <td><a href="#" class="btn btn-danger btn-sm delete">x</a></td>
        `;

        list.appendChild(row);
    }

    static showAlert(message, className) {
        const div = document.createElement('div');
        div.className = `alert alert-${className}`;
        div.appendChild(document.createTextNode(message));
        const container = document.querySelector(".container");
        const form = document.getElementById('book-form');
        container.insertBefore(div, form);

        // set time to vanish
        setTimeout(() => document.querySelector('.alert').remove(), 2000);
    }

    static deleteBook(list_item) {
        if (list_item.classList.contains("delete")) {
            list_item.parentElement.parentElement.remove();
        }
    }

    static clearFields() {
        document.getElementById("title").value = "";
        document.getElementById("author").value = "";
        document.getElementById("isbn").value = "";
    }
}

// store class: handles storage
class Store {
    static getBooks() {
        let books;
        if (localStorage.getItem('books') === null) {
            books = [];
        }
        else{
            books = JSON.parse(localStorage.getItem('books'));
        }
        return books;
    }

    static addBook(book) {
        const books = Store.getBooks();
        books.push(book);
        localStorage.setItem("books", JSON.stringify(books));
    }

    static removeBook(isbn) {  
        const books = Store.getBooks();
        books.forEach((book, index) => {
            if (book.isbn === isbn) {
                books.splice(index, 1);
            }
        });
        localStorage.setItem('books', JSON.stringify(books));
    }
}

// Event: display books
document.addEventListener('DOMContentLoaded', UI.displayBooks);

// Event: Add a book
document.getElementById("book-form").addEventListener('submit', (e) => {
    e.preventDefault();
    const title = document.getElementById("title").value;
    const author = document.getElementById("author").value;
    const isbn = document.getElementById("isbn").value;

    // validation
    if (title === "" || author === "" || isbn === "") {
        UI.showAlert("Please fill all the fields", "danger")
    }
    else {
        const newBook = new Book(title, author, isbn);
        UI.addBookToList(newBook);
        Store.addBook(newBook);
        UI.showAlert("Book Added", "success");
        UI.clearFields();
    }

});

// Event: Remove a book
document.getElementById("book-list").addEventListener('click', (e) => {
    UI.deleteBook(e.target);
    Store.removeBook(e.target.parentElement.previousElementSibling.textContent);
    UI.showAlert("Book removed", "success")
})