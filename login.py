import flet as ft
import hashlib
import firebase_admin
from firebase_admin import credentials, auth,  firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("/Users/danielshirazi/Downloads/bitebuddies-8d6f6-firebase-adminsdk-ald1c-229148601d.json")  # Replace with your Firebase Admin SDK JSON file path
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()  # This sets up `db` to be used throughout your code

# Utility function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Sign up function
def signup(email, password):
    try:
        # Check if the email already exists in Firestore
        users_ref = db.collection("Users").where("email", "==", email).get()
        if len(users_ref) > 0:
            return "Error: Email already registered."
        
        # Hash the password
        hashed_password = hash_password(password)
        
        # Create user in Firebase Auth
        user = auth.create_user(email=email, password=password)
        
        # Store user details in Firestore
        db.collection("Users").document(user.uid).set({
            "email": email,
            "password_hash": hashed_password
        })
        
        return f"User created with UID: {user.uid}"
    except Exception as e:
        return f"Error: {str(e)}"
    
# Login function
def login(email, password):
    try:
        # Retrieve the user by email from Firestore
        users_ref = db.collection("Users").where("email", "==", email).get()
        if len(users_ref) == 0:
            return "Error: Email not registered."
        
        # Get the hashed password
        user_doc = users_ref[0]
        stored_hash = user_doc.get("password_hash")
        
        # Hash the entered password
        entered_hash = hash_password(password)
        
        # Verify the hashes match
        if stored_hash == entered_hash:
            return f"Logged in as: {user_doc.id}"  # Return the user's UID
        else:
            return "Error: Invalid password."
    except Exception as e:
        return f"Error: {str(e)}"

# Page for sign up/login options
def show_signup_page(page, function):
    page.clean()  # Clear the current page
    email_input = ft.TextField(label="Email", autofocus=True, width=300)
    password_input = ft.TextField(label="Password", password=True, width=300)
        
    result_text = ft.Text()

    def handle_signup(e):
        email = email_input.value
        password = password_input.value
        if email and password:
            result = signup(email, password)
            result_text.value = result
            page.update()
            function()
        else:
            result_text.value = "Please enter both email and password."
            page.update()

    signup_button = ft.ElevatedButton("Sign Up", on_click=handle_signup)
    page.add(email_input, password_input, signup_button, result_text)

def show_login_page(page, function):
    page.clean()  # Clear the current page
    email_input = ft.TextField(label="Email", autofocus=True, width=300)
    password_input = ft.TextField(label="Password", password=True, width=300)
        
    result_text = ft.Text()

    def handle_login(e):
        email = email_input.value
        password = password_input.value
        if email and password:
            result = login(email, password)
            result_text.value = result
            page.update()
            function()
        else:
            result_text.value = "Please enter both email and password."
            page.update()

    login_button = ft.ElevatedButton("Login", on_click=handle_login)
    page.add(email_input, password_input, login_button, result_text)

    # Page to ask whether user wants to login or signup
def ask_signup_or_login(page, function):
    page.clean()
    label = ft.Text("Would you like to Sign Up or Login?")
    signup_button = ft.ElevatedButton("Sign Up", on_click=lambda e: show_signup_page(page, function))
    login_button = ft.ElevatedButton("Login", on_click=lambda e: show_login_page(page, function))
    page.add(label, signup_button, login_button)