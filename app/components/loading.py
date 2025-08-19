import flet as ft
import time


class Loading(ft.Container):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.height = 50
        self.width = 1400 // 2
        self.bgcolor = ft.Colors.GREY_100
        self.expand = True
        self.border_radius = ft.border_radius.all(10)
        self.padding = ft.padding.all(10)
        self.margin = ft.margin.only(bottom=10)
        self.animate = ft.Animation(
            duration=600,
            curve=ft.AnimationCurve.DECELERATE,
        )
        self.state_scale = 1

    def infinite_animation(self):
        while True:
            if self.state_scale == 1:
                self.scale = ft.transform.Scale(0.7)
                self.state_scale = 0
            else:
                self.scale = ft.transform.Scale(1)
                self.state_scale = 1
            self.update()
            time.sleep(0.6)
