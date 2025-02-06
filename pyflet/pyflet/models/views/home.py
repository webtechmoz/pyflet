from controls.controls import (
    ft,
    DateTime,
    Text,
    View
)

import asyncio

class Home(View):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__(page=page, route='/')
        self.datatime = DateTime()
        self.controls = [
            ft.Column(
                controls=[
                    ft.Container(
                        image=ft.DecorationImage(
                            src='flet.png',
                            fit=ft.ImageFit.COVER
                        ),
                        width=100,
                        height=100,
                        border_radius=100,
                        border=ft.border.all(
                            width=1,
                            color=ft.Colors.with_opacity(0.40, 'grey')
                        )
                    ),
                    Text(
                        value=self.page.title,
                        size=22,
                        weight='bold'
                    ),
                    time_text := Text(
                        value=f'{self.datatime.date}, {self.datatime.hour}',
                        size=16
                    )
                ],
                spacing=5,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]

        self.time_text = time_text
    
    async def update_time(self, e: ft.ControlEvent):
        while True:
            self.datatime = DateTime()

            self.time_text.value = f'{self.datatime.date}, {self.datatime.hour}'
            
            e.update()
            await asyncio.sleep(1)
