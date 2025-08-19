import flet as ft
from app.components import Header
from app.screens import HomeScreen, NavigationScreen
from app.providers import ScreenStackProvider

#  flet run main.py
def main(page: ft.Page):
    page.title = "AI Agent Chat"
    page.window.height = 600
    page.window.width = 1200
    page.window.center()

    screen_stack = ScreenStackProvider()

    # Header gọi toggle_sidebar thay vì chỉ shrink
    header = Header(on_toggle=screen_stack.home_screen.toggle_sidebar)

    page.add(header, screen_stack)

if __name__ == "__main__":
    ft.app(target=main)
