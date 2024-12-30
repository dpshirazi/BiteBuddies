import flet as ft
import login
import dashboard

def main(page):
    page.title = "Welcome to BiteBuddies"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Ensure you call `ask_signup_or_login` with `on_success` explicitly
    #login.ask_signup_or_login(page, dashboard.interface(page))
    dashboard.interface(page)
ft.app(target=main)