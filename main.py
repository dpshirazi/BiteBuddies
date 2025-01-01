import flet as ft
import login
import dashboard

def main(page):
    # Set up the page's general properties
    page.title = "Welcome to BiteBuddies"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Function to handle successful login
    def after_successful_login():
        # Clear the page and show the dashboard
        page.controls.clear()
        dashboard.interface(page)  # Call the dashboard interface
        page.update()

    # Ensure login/signup is the first screen
    page.controls.clear()
    login.ask_signup_or_login(page, after_successful_login)
    page.update()

# Start the app
ft.app(target=main)
