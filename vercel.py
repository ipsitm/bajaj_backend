from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    try:
        data = request.json.get('data', [])
        
        if not isinstance(data, list):
            return jsonify({
                "is_success": False,
                "user_id": "ipsit_maurya_10122002",
                "message": "Invalid input. 'data' must be a list."
            }), 400

        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]

        lowercase_alphabets = [item for item in alphabets if item.islower()]
        highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else ""

        response = {
            "is_success": True,
            "user_id": "ipsit_maurya_10122002",
            "email": "ipsit.maurya2021@vitstudent.ac.in",
            "roll_number": "21BCE5390",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
        }

        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            "is_success": False,
            "user_id": "ipsit_maurya_10122002",
            "message": str(e)
        }), 500

@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({"operation_code": 1}), 200
