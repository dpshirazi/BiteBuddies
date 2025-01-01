import flet as ft
import bite  # Make sure this is the correct import for your bite.py file

def interface(page: ft.Page):
    # Set the page title and layout
    page.title = "Bite Buddies Dashboard"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START  # Align left

    # Create friends section
    friends_section = ft.Column(
        [
            ft.Text("Friends", size=20, weight=ft.FontWeight.BOLD),
            ft.ListView(
                [
                    ft.Row([ft.Text("John Doe"), ft.IconButton(ft.icons.ADD, on_click=add_friend)]),
                    ft.Row([ft.Text("Jane Smith"), ft.IconButton(ft.icons.ADD, on_click=add_friend)]),
                ]
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
    )

    # Create a dynamic list for bites
    bites_list = ft.Column(spacing=10)

    def create_new_bite(): 
        # Pass the page and bites_list to the function correctly
        bite.create_new_bite(page, bites_list)

    # Create "Create New Bite" button
    create_bite_button = ft.ElevatedButton("Create New Bite", on_click=lambda e: create_new_bite())

    # Adjust layout
    page.add(
        ft.Column(
            [
                # Friends section with padding and fixed size
                ft.Container(
                    friends_section,
                    width=300,  # Width of the section
                    height=250,  # Height of the section
                    padding=10,
                ),

                # Create New Bite button with padding
                create_bite_button,
                bites_list  # Add the dynamic list to the page
            ],
            spacing=20,  # Space between the two containers
            alignment=ft.MainAxisAlignment.START  # Align the entire column to the top
        )
    )

def add_friend(e):
    # Placeholder for adding friends (could trigger a form or Firebase logic)
    print("Add friend clicked!")


