from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, auth

# Initialize Flask app
app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate('/Users/danielshirazi/Downloads/bitebuddies-8d6f6-firebase-adminsdk-ald1c-229148601d.json')  # Update this with the correct path to your JSON file
firebase_admin.initialize_app(cred)

@app.route('/signup', methods=['POST'])
def signup():
    email = request.json.get('email')
    password = request.json.get('password')
    try:
        # Use Firebase Admin SDK to create user
        user = auth.create_user(
            email=email,
            password=password
        )
        return jsonify({"message": "User created", "user_id": user.uid}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
