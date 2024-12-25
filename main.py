import flet as ft

import firebase_admin
from firebase_admin import credentials

# Initialize Firebase Admin SDK with service account credentials
cred = credentials.Certificate("/Users/danielshirazi/Downloads/bitebuddies-8d6f6-firebase-adminsdk-ald1c-229148601d.json")
firebase_admin.initialize_app(cred)




def main(page: ft.Page):
    page.title = "Lunch Matching App"
    page.add(ft.Text("Hello, world!"))

ft.app(target=main)
