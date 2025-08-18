import flet as ft
from app.animations import AnimationUtils

class HomeScreen(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.width = 1200
        self.bgcolor = ft.Colors.WHITE
        self.expand = True
        self.is_shrunk = False  # trạng thái sidebar

        self.animate_scale = ft.Animation(
            duration=500, curve=ft.AnimationCurve.DECELERATE
        )

        self.content = ft.Column(
            controls=[
                ft.Text("Welcome to the Home Screen", size=30),
                ft.ElevatedButton("Get Started", on_click=self.start_clicked),
            ]
        )

    def start_clicked(self, e):
        print("Get Started button clicked")

    def toggle_sidebar(self, event: ft.ControlEvent):
        if self.is_shrunk:
            AnimationUtils.animation_grow(self, event)
            self.is_shrunk = False
        else:
            AnimationUtils.animation_shrink(self, event)
            self.is_shrunk = True
