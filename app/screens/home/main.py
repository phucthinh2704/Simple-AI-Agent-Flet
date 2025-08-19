import flet as ft
from app.animations import AnimationUtils
from app.components import MessageCard, Loading
from app.model_llm import get_answer


class HomeScreen(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.width = 1400
        self.bgcolor = ft.Colors.WHITE
        self.expand = True
        self.animate_scale = ft.Animation(
            duration=600, curve=ft.AnimationCurve.DECELERATE
        )
        self.border_radius = ft.border_radius.all(10)
        self.padding = ft.padding.all(10)

        # ListView chiếm toàn bộ chiều cao còn lại
        self.content_chats = ft.ListView(
            expand=True,
            width=self.width,
            controls=[
                MessageCard("ai", message="Hello, how can I help you?"),
                MessageCard("human", message="I need help with my account."),
            ],
        )

        self.text_field = ft.TextField(
            hint_text="Type a message",
            expand=True,
        )

        self.input_chat = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(
                        name=ft.Icons.INSERT_EMOTICON,
                        size=24,
                    ),
                    self.text_field,
                    ft.IconButton(
                        icon=ft.Icons.SEND,
                        icon_size=24,
                        on_click=self.handle_chat,
                    ),
                ],
            ),
        )

        self.content = ft.Column(
            expand=True,
            controls=[
                self.content_chats,
                self.input_chat,
            ],
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

    def handle_chat(self, event: ft.ControlEvent):
        loading = Loading()
        self.content_chats.controls.extend(
            [
                MessageCard("human", message=self.text_field.value),
                loading,
            ]
        )
        self.content_chats.update()

        answer_from_ai = get_answer(self.text_field.value)
        self.content_chats.controls.pop()
        self.content_chats.controls.append(MessageCard("ai", message=answer_from_ai))
        self.content_chats.update()
