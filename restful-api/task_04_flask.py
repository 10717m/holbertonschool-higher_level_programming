from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize users dictionary (empty for submission)
users = {}

@app.route('/')
def home():
    """Root endpoint that returns a welcome message"""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Endpoint that returns list of usernames"""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Endpoint that returns API status"""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Endpoint that returns user data by username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Endpoint to add new users via POST request"""
    data = request.get_json()
    
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data['username']
    users[username] = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
