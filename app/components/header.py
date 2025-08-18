import flet as ft

class Header(ft.Container):
    def __init__(self, on_toggle):
        super().__init__()
        self.height = 50
        self.width = 1200
        self.bgcolor = ft.Colors.DEEP_PURPLE_400
        self.border_radius = ft.border_radius.all(10)
        self.padding = ft.padding.only(right=10)

        self.content = ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.MENU,
                    icon_size=24,
                    icon_color=ft.Colors.WHITE,
                    on_click=on_toggle,  # gọi toggle_sidebar
                ),
                ft.CircleAvatar(
                    content=ft.Icon(
                        ft.Icons.PERSON, size=24, color=ft.Colors.DEEP_ORANGE_200
                    ),
                    bgcolor=ft.Colors.WHITE,
                    radius=20,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
