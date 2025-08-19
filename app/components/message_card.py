import flet as ft
from typing import Literal

Options = Literal["ai", "human"]


class MessageCard(ft.Container):
    def __init__(self, options: Options, **kwargs):
        super().__init__()
        self.options = options
        self.animate = ft.Animation(
            duration=600,
            curve=ft.AnimationCurve.DECELERATE,
        )
        self.width = 1400 // 2

        self.content_chat = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(
                        name=(
                            ft.Icons.COMPUTER
                            if self.options == "ai"
                            else ft.Icons.PERSON
                        ),
                        size=24,
                    ),
                    ft.Markdown(
                        value=kwargs.get("message", "# Message"),
                        width=self.width,
                    ),
                ],
            ),
            padding=ft.padding.all(10),
            bgcolor=ft.Colors.GREY_100 if self.options == "ai" else ft.Colors.GREY_300,
            border_radius=ft.border_radius.all(10),
            margin=ft.margin.only(bottom=10),
        )

        self.content = ft.Row(
            controls=[self.content_chat],
            alignment=(
                ft.MainAxisAlignment.START
                if self.options == "ai"
                else ft.MainAxisAlignment.END
            ),
        )
