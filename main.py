import flet as ft
import login
import dashboard



def main(page):
    page.title = "Welcome to BiteBuddies"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    def after_successful_login(): 
        page.controls.clear()
        dashboard.interface(page)

    # Ensure you call `ask_signup_or_login` with `on_success` explicitly
    login.ask_signup_or_login(page, after_successful_login)
ft.app(target=main)