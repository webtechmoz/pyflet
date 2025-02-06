from views.home import ft, Home, asyncio

def main(page: ft.Page):
    page.title = 'project title'

    home = Home(page=page)

    def router(route: str):
        page.views.clear()

        if page.route == '/':
            page.views.append(home)
        
        page.update()
    
    page.on_route_change = router
    page.go(page.route)
    asyncio.run(home.update_time(page))

if __name__ == '__main__':
    ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER,
        assets_dir='assets',
        upload_dir='assets',
        use_color_emoji=True
    )