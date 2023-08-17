from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user data for demonstration purposes. In real life, use a database!
users = {
    'admin': 'password123'
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify({'message': 'Login successful!'})
    else:
        return jsonify({'message': 'Invalid credentials!'}), 401
      
@app.route('/get_first_name', methods=['GET'])
def get_first_name():
    # For demonstration purposes, returning a static first name.
    # In a real-world scenario, this could come from a database or another source.
    return jsonify({"first_name": "John"})

if __name__ == '__main__':
    app.run(debug=True)
