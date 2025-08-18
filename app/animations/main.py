import flet as ft


class AnimationUtils:
    @staticmethod
    def animation_shrink(obj: ft.Control, event: ft.ControlEvent):
        obj.scale = ft.Scale(0.65, alignment=ft.alignment.center_right)
        obj.update()

    @staticmethod
    def animation_grow(obj: ft.Control, event: ft.ControlEvent):
        obj.scale = ft.Scale(1, alignment=ft.alignment.center_right)
        obj.update()
