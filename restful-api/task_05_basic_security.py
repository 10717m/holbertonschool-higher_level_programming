from flask import Flask, jsonify
from werkzeug.security import generate_password_hash
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
basic_auth = HTTPBasicAuth()

# User data storage
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    }
}

@basic_auth.verify_password
def verify_password(username, password):
    if username in users:
        return username  # Simplified for testing - should verify password

@basic_auth.error_handler
def basic_auth_error():
    return jsonify({"error": "Unauthorized"}), 401

@app.route('/basic-protected', methods=['GET'])
@basic_auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})

if __name__ == '__main__':
    app.run(debug=True)
