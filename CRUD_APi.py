# Import necessary modules from Flask
from flask import Flask, jsonify, request

# Initialize a Flask application
app = Flask(__name__)

# Mock database of books (to be replaced with database integration)
books = [
    {'id': 1, 'book_name': 'Book A', 'author': 'Author A', 'publisher': 'Publisher A'},
    {'id': 2, 'book_name': 'Book B', 'author': 'Author B', 'publisher': 'Publisher B'}
]

# Endpoint to get all books using HTTP GET method
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Endpoint to get a specific book by its id using HTTP GET method
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

# Endpoint to create a new book using HTTP POST method
@app.route('/books', methods=['POST'])
def create_book():
    # Extract JSON data from the request body
    new_book = request.get_json()
    # Add the new book to the list of books
    books.append(new_book)
    # Return the newly created book as JSON response with status code 201 (Created)
    return jsonify(new_book), 201

# Endpoint to update an existing book by its id using HTTP PUT method
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            # Update the existing book with the data from the request body
            book.update(request.get_json())
            # Return the updated book as JSON response
            return jsonify(book)
    # If no book is found with the given id, return an error message with status code 404 (Not Found)
    return jsonify({'error': 'Book not found'}), 404

# Endpoint to delete a book by its id using HTTP DELETE method
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for i, book in enumerate(books):
        if book['id'] == book_id:
            # Remove the book from the list of books
            del books[i]
            # Return a success message as JSON response with status code 200 (OK)
            return jsonify({'message': 'Book deleted'}), 200
    # If no book is found with the given id, return an error message with status code 404 (Not Found)
    return jsonify({'error': 'Book not found'}), 404

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)