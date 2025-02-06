import flet as ft
from datetime import datetime

class View(ft.View):
    def __init__(
        self,
        page: ft.Page,
        route: str
    ):
        super().__init__()
        self.page = page
        self.route = route
        self.bgcolor = ft.Colors.WHITE
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.padding = ft.padding.all(0)

class Text(ft.Text):
    def __init__(
        self,
        value: str,
        color: ft.Colors = ft.Colors.with_opacity(0.80, 'black'),
        size: float = 14,
        weight: ft.FontWeight = ft.FontWeight.W_600,
        selectable: bool = False
    ):
        super().__init__()
        self.value = value
        self.color = color
        self.weight = weight
        self.size = size
        self.selectable = selectable

class DateTime():
    def __init__(
        self
    ):
        self.__now = datetime.now()
        self.date = self.__now.strftime("%d/%m/%Y")
        self.hour = self.__now.strftime("%H:%M:%S")
