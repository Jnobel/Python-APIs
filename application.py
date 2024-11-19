from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)

# Use the application context to create the database
with app.app_context():
    db.create_all()

# Create a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(
        book_name=data['book_name'],
        author=data['author'],
        publisher=data['publisher']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book added successfully!"}), 201

# Read all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {
            'id': book.id,
            'book_name': book.book_name,
            'author': book.author,
            'publisher': book.publisher
        }
        output.append(book_data)
    return jsonify({"books": output})

# Read a single book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({
        'id': book.id,
        'book_name': book.book_name,
        'author': book.author,
        'publisher': book.publisher
    })

# Update a book by ID
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = Book.query.get_or_404(id)
    book.book_name = data['book_name']
    book.author = data['author']
    book.publisher = data['publisher']
    db.session.commit()
    return jsonify({"message": "Book updated successfully!"})

# Delete a book by ID
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)