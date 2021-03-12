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
    constructor() {

    }
    static displayBooks() {
        const StoredBooks = [
            {
                title: 'Book one',
                author: 'John Doe',
                isbn: '32121'
            },
            {
                title: 'Book two',
                author: 'John Cena',
                isbn: '637829'
            }
        ];
        const books = StoredBooks;
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
}

// store class: handles storage

// Event: display books
document.addEventListener('DOMContentLoaded', UI.displayBooks);

// Event: Add a book
document.getElementById("book-form").addEventListener('submit', (e) => {
    e.preventDefault();
    const title = document.getElementById("title").value;
    const author = document.getElementById("author").value;
    const isbn = document.getElementById("isbn").value;

    const newBook = new Book(title, author, isbn);

    console.log(newBook);
});

// Event: Remove a book