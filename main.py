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
    
    page.horizontal_alignment='center'
    page.vertical_alignment='center'

    p_ring = ft.ProgressRing(
        color=ft.colors.GREEN_ACCENT_700,
        bgcolor=ft.colors.AMBER_200

    )

    page.add(p_ring)
    
    lv = ft.ListView(expand=1, spacing=10, padding=20)

    news  = fetch_news()

    page.update()
    
    for n in news:
        lv.controls.append(
            ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.NEWSPAPER),
                            title=ft.Text(n['title']),
                            subtitle=ft.Text(
                                n['url']
                            )
                        )
                    ]
                ),
                expand=True,
                padding=10,
                border=ft.border.all(width=3,color=ft.colors.GREEN_ACCENT_700),
                border_radius=10
            )
        )
        )
        
    page.add(lv)

ft.app(target=main)