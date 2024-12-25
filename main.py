import flet as ft

def main(page: ft.Page):
    page.title = "Lunch Matching App"
    page.add(ft.Text("Hello, world!"))

ft.app(target=main)
