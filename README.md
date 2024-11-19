Book API Project
This is a simple RESTful API built using Flask and SQLAlchemy that allows you to perform CRUD (Create, Read, Update, Delete) operations on a collection of books. It is intended to demonstrate how to create a basic API using Python and Flask.

Features
Add a Book: Create new book entries in the database.
View All Books: Retrieve a list of all books.
View a Single Book: Get details of a specific book by its ID.
Update a Book: Modify the details of an existing book.
Delete a Book: Remove a book from the database.
Technologies Used
Python: Programming language
Flask: Web framework for building the API
Flask-SQLAlchemy: ORM for database interaction
SQLite: Lightweight database for data storage
Installation and Setup
Prerequisites
Python (version 3.6 or higher)
Virtual environment (optional but recommended)

Steps to Set Up the Project
Clone the Repository

bash
Copy code
git clone https://github.com/your-username/book-api.git
cd book-api
Set Up a Virtual Environment

bash
Copy code
python -m venv myenv
source myenv/Scripts/activate  # On Windows
source myenv/bin/activate      # On macOS/Linux
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Run the Application

bash
Copy code
flask --app application.py run
The server will be running at http://127.0.0.1:5000/.

API Endpoints
1. Create a Book
URL: /books
Method: POST
Request Body: JSON
json
Copy code
{
    "book_name": "Example Book",
    "author": "Author Name",
    "publisher": "Publisher Name"
}
Response: Success message with status 201
2. Get All Books
URL: /books
Method: GET
Response: List of all books
3. Get a Book by ID
URL: /books/<id>
Method: GET
Response: Book details
4. Update a Book
URL: /books/<id>
Method: PUT
Request Body: JSON
json
Copy code
{
    "book_name": "Updated Book Name",
    "author": "Updated Author",
    "publisher": "Updated Publisher"
}
Response: Success message
5. Delete a Book
URL: /books/<id>
Method: DELETE
Response: Success message
Usage
You can test the API using tools like Postman or cURL.

Example cURL Commands
Add a New Book

bash
Copy code
curl -X POST http://127.0.0.1:5000/books -H "Content-Type: application/json" -d '{"book_name": "1984", "author": "George Orwell", "publisher": "Secker & Warburg"}'
Get All Books

bash
Copy code
curl -X GET http://127.0.0.1:5000/books
Get a Book by ID

bash
Copy code
curl -X GET http://127.0.0.1:5000/books/1
Update a Book

bash
Copy code
curl -X PUT http://127.0.0.1:5000/books/1 -H "Content-Type: application/json" -d '{"book_name": "Updated Book", "author": "Updated Author", "publisher": "Updated Publisher"}'
Delete a Book

bash
Copy code
curl -X DELETE http://127.0.0.1:5000/books/1
Contributing
Feel free to submit issues or pull requests if you'd like to contribute to the project. Contributions are welcome!

License
This project is licensed under the  Apache License Version 2.0,  License. See the LICENSE file for more information.

Acknowledgments
The Flask and Flask-SQLAlchemy documentation
REST API tutorials and resources for inspiration
