from flask import request, jsonify
from db import app, get_db  # use get_db() instead of mysql

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    cur.close()
    return jsonify(books)

# Add new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    cur = get_db().cursor()
    cur.execute("INSERT INTO books(title, author) VALUES(%s, %s)", (data['title'], data['author']))
    get_db().commit()
    cur.close()
    return jsonify({"message": "Book added successfully"})
