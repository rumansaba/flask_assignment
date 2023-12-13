from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for books
books = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
    {'id': 3, 'title': '1984', 'author': 'George Orwell'}
]

# Routes for HTML pages

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        data = request.form
        new_book = {'id': len(books) + 1, 'title': data['title'], 'author': data['author']}
        books.append(new_book)
        return render_template('index.html', books=books, message='Book added successfully')

    return render_template('add_book.html')

@app.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return render_template('index.html', books=books, error='Book not found')

    if request.method == 'POST':
        data = request.form
        book['title'] = data['title']
        book['author'] = data['author']
        return render_template('index.html', books=books, message='Book updated successfully')

    return render_template('edit_book.html', book=book)

@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return render_template('index.html', books=books, message='Book deleted successfully')

# Routes for RESTful API

@app.route('/api/books', methods=['GET'])
def get_books_api():
    return jsonify({'books': books})

@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book_api(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({'message': 'Book not found'}), 404
    return jsonify({'book': book})

@app.route('/api/books', methods=['POST'])
def create_book_api():
    data = request.get_json()
    new_book = {'id': len(books) + 1, 'title': data['title'], 'author': data['author']}
    books.append(new_book)
    return jsonify({'message': 'Book created successfully', 'book': new_book}), 201

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book_api(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({'message': 'Book not found'}), 404

    data = request.get_json()
    book['title'] = data['title']
    book['author'] = data['author']

    return jsonify({'message': 'Book updated successfully', 'book': book})

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book_api(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
