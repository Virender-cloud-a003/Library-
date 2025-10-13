from flask import request, jsonify
from db import app, get_db  # use get_db() instead of mysql

# Get all members
@app.route('/members', methods=['GET'])
def get_members():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM members")
    members = cur.fetchall()
    cur.close()
    return jsonify(members)

# Add new member
@app.route('/members', methods=['POST'])
def add_member():
    data = request.json
    cur = get_db().cursor()
    cur.execute("INSERT INTO members(name,email) VALUES(%s,%s)", (data['name'], data['email']))
    get_db().commit()
    cur.close()
    return jsonify({"message": "Member added successfully"})
