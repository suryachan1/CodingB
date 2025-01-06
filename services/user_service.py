from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
import jwt
import datetime

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = 'your_secret_key'

users = {}  # In-memory storage

@app.route('/user/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    users[data['username']] = {'password': hashed_password}
    return jsonify({"message": "User registered"}), 201

@app.route('/user/login', methods=['POST'])
def login():
    data = request.json
    user = users.get(data['username'])
    if user and bcrypt.check_password_hash(user['password'], data['password']):
        token = jwt.encode(
            {'username': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            app.config['SECRET_KEY']
        )
        return jsonify({"token": token})
    return jsonify({"message": "Invalid credentials"}), 401
  
