from flask import Flask, request, jsonify, redirect, url_for, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'userinfo'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Create User Table if not exists
cursor = mysql.connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) UNIQUE,
                    password VARCHAR(255),
                    email VARCHAR(255)
                  )''')
mysql.connection.commit()
cursor.close()

# Register endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for('home'), code=302)

# Home endpoint
@app.route('/')
def home():
    # Logic to return products
    return jsonify({"products": ["product1", "product2", "product3"]}), 200

# Get user by username or userId endpoint
@app.route('/user/<identifier>', methods=['GET'])
def get_user(identifier):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s OR id = %s", (identifier, identifier))
    user = cursor.fetchone()
    cursor.close()

    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

# Update user information endpoint
@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    # Logic to update user information
    return jsonify({"message": "User information updated successfully"}), 200

# Delete user account endpoint
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Logic to delete user account
    return jsonify({"message": "User account deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)