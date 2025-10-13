from flask import request, jsonify
from db import app, get_db  # use get_db() instead of mysql
from datetime import date

# Borrow a book
@app.route('/borrow', methods=['POST'])
def borrow_book():
    data = request.json
    book_id = data['book_id']
    member_id = data['member_id']
    borrow_date = data.get('borrow_date', str(date.today()))
    
    cur = get_db().cursor()
    # Update book status
    cur.execute("UPDATE books SET status='Issued' WHERE id=%s", (book_id,))
    # Add borrow record
    cur.execute("INSERT INTO borrow(book_id, member_id, borrow_date) VALUES(%s,%s,%s)",
                (book_id, member_id, borrow_date))
    get_db().commit()
    cur.close()
    return jsonify({"message": "Book borrowed successfully"})
