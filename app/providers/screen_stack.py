import flet as ft
from ..screens import HomeScreen, NavigationScreen


class ScreenStackProvider(ft.Stack):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.home_screen = HomeScreen()
        self.navigation_screen = NavigationScreen()
        self.controls = [self.navigation_screen, self.home_screen]
        self.expand = True
