from flask import Flask, request, jsonify

app = Flask(__name__)
blogs = {}  # In-memory storage
counter = 1

@app.route('/blog', methods=['POST'])
def create_blog():
    global counter
    data = request.json
    blogs[counter] = data
    counter += 1
    return jsonify({"message": "Blog created"}), 201

@app.route('/blog', methods=['GET'])
def list_blogs():
    return jsonify(blogs), 200
  
