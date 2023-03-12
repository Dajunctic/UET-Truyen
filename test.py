import os
import flet as ft
from settings import *
from src.theme.sub_theme.chapter import *
from src.theme.footer import *
from src.theme.header import *
from src.theme.navbar import *

class App:
    def __init__(self):
        self.chapter = Chapter(os.getcwd())
        self.footer = Footer()
        self.header = Header()
        self.navbar = NavBar()

    def run(self, page: ft.Page):
        page.title = TITLE
        page.bgcolor = ft.colors.WHITE
        page.scroll = "always"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        page.add(self.header.content, self.navbar.content, self.chapter.content, self.footer.content)


if __name__ == '__main__':
    app = App()
    ft.app(target=app.run, assets_dir="assets")
    # ft.app(target=app.run, view=ft.WEB_BROWSER, assets_dir="assets")
