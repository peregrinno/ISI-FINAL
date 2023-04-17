from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/api/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def create_user():
    user = request.get_json()
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (user['name'], user['email']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'User created successfully!'})

@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = request.get_json()
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("UPDATE users SET name=?, email=? WHERE id=?", (user['name'], user['email'], id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'User updated successfully!'})

@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'User deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
