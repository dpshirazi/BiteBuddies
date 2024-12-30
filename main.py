import flet as ft
import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase Admin SDK
cred = credentials.Certificate('/Users/danielshirazi/Downloads/bitebuddies-8d6f6-firebase-adminsdk-ald1c-229148601d.json')  # Update with your Firebase Admin SDK path
firebase_admin.initialize_app(cred)

# Define the sign-up function that interacts with Firebase
def signup(email, password):
    try:
        # Create the user using Firebase Admin SDK
        user = auth.create_user(email=email, password=password)
        return f"User created with UID: {user.uid}"
    except Exception as e:
        return f"Error: {str(e)}"

# Define the Flet app
def main(page):
    page.title = "Firebase Sign-Up"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Create input fields and buttons for the sign-up form
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
        else:
            result_text.value = "Please enter both email and password."
            page.update()
    
    # Create the submit button
    signup_button = ft.ElevatedButton("Sign Up", on_click=handle_signup)
    
    # Add the elements to the page
    page.add(email_input, password_input, signup_button, result_text)

# Start the Flet app
ft.app(target=main)
