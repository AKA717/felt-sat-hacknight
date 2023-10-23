import flet as ft
from scrape import fetch_news

def main(page):
    page.title = "BestOfHackerNews"

    page.add(ft.Text(
            "HackerNews",
            size=20,
            color=ft.colors.TEAL_ACCENT_200,
            weight=ft.FontWeight.BOLD,
        ))
    
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    news  = fetch_news()
    
    for n in news:
        lv.controls.append(
            ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text(n['title']),
                            subtitle=ft.Text(
                                n['url']
                            )
                        )
                    ]
                ),
                expand=True,
                padding=10,
            )
        )
        )
        
    page.add(lv)

ft.app(target=main)