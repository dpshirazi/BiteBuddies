import flet as ft

def create_new_bite(page: ft.Page, bites_list: ft.Column):
    # Function to handle the submission of the new bite
    def save_bite(e):
        if time_input.value and location_input.value:
            # Add the new bite to the bites list and update the UI
            new_bite = ft.Row(
                [
                    ft.Text(f"Time: {time_input.value}"),
                    ft.Text(f"Location: {location_input.value}"),
                    ft.Text(f"Preference: {'Friends' if preference_switch.value else 'Strangers'}"),
                ],
                spacing=10,
            )
            bites_list.controls.append(new_bite)
            bites_list.update()  # Update the list on the page
            print(f"Saved Bite - Time: {time_input.value}, Location: {location_input.value}, Preference: {'Friends' if preference_switch.value else 'Strangers'}")
            # Close the dialog
            dialog.open = False
            page.update()
        else:
            print("Please fill in all fields!")

    # Input fields for time, location, and preference
    time_input = ft.TextField(label="Time (e.g., 12:30 PM)", width=300)
    location_input = ft.TextField(label="Location (e.g., Dining Hall A)", width=300)
    preference_switch = ft.Switch(label="Eat with Friends", value=True)

    # Create the dialog
    dialog = ft.AlertDialog(
        title=ft.Text("Create New Bite"),
        content=ft.Column(
            [
                time_input,
                location_input,
                preference_switch,
            ],
            spacing=20,
        ),
        actions=[
            ft.TextButton("Save", on_click=save_bite),
            ft.TextButton("Cancel", on_click=lambda e: close_dialog()),
        ],
        modal=True,
    )

    # Function to close the dialog
    def close_dialog():
        dialog.open = False
        page.update()

    # Open the dialog
    page.dialog = dialog
    dialog.open = True
    page.update()


def interface(page: ft.Page):
    page.title = "Bite Buddies Dashboard"
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Create a dynamic list for bites
    bites_list = ft.Column(spacing=10)

    # Create "Create New Bite" button
    create_bite_button = ft.ElevatedButton("Create New Bite", on_click=lambda e: create_new_bite(page, bites_list))

    # Add components to the page
    page.add(
        ft.Column(
            [
                create_bite_button,
                ft.Text("Bites List", size=20, weight=ft.FontWeight.BOLD),
                bites_list,  # Add the dynamic list to the page
            ],
            spacing=20,
        )
    )
