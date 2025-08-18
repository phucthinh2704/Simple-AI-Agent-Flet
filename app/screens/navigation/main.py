import flet as ft


class NavigationScreen(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.width = 1200
        self.bgcolor = ft.Colors.WHITE
        self.expand = True

        self.content = ft.Column(
            controls=[
                ft.Text("Navigation Screen", size=30),
                ft.ElevatedButton("Go to Home", on_click=self.go_home_clicked),
            ]
        )

    def go_home_clicked(self, e):
        print("Go to Home button clicked")
