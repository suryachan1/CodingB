from flask import Flask, request, jsonify

app = Flask(__name__)
comments = {}  # In-memory storage

@app.route('/comment', methods=['POST'])
def add_comment():
    data = request.json
    post_id = data['post_id']
    if post_id not in comments:
        comments[post_id] = []
    comments[post_id].append(data['comment'])
    return jsonify({"message": "Comment added"}), 201

@app.route('/comment', methods=['GET'])
def get_comments():
    post_id = request.args.get('post_id')
    return jsonify(comments.get(int(post_id), [])), 200
  
