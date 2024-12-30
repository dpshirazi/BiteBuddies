import flet as ft

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

    # Create "Create New Bite" button
    create_bite_button = ft.ElevatedButton("Create New Bite", on_click=create_new_bite)

    # Adjust layout
    page.add(
        ft.Column(
            [
                # Friends section with fixed width
                ft.Container(friends_section, width=300, height=200, padding=10),

                # Create New Bite button with padding
                ft.Container(create_bite_button, padding=20),
            ],
            spacing=20,  # Space between the two containers
        )
    )

def add_friend(e):
    # Placeholder for adding friends (could trigger a form or Firebase logic)
    print("Add friend clicked!")

def create_new_bite(e):
    # Placeholder for the "Create New Bite" functionality
    print("Create new bite clicked!")