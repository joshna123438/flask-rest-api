from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    users.append(data)
    return {"message": "User added"}

@app.route('/users/<int:index>', methods=['PUT'])
def update_user(index):
    users[index] = request.json
    return {"message": "User updated"}

@app.route('/users/<int:index>', methods=['DELETE'])
def delete_user(index):
    users.pop(index)
    return {"message": "User deleted"}

app.run(debug=True)
