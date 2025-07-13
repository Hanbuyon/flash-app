from flet import *

def main(page: Page):
    page.title = "Flash App"
    page.scroll = 'auto'
    page.window.top = 1
    page.window.left = 960
    page.window.width = 390
    page.window.height = 740
    page.bgcolor= 'white'
    page.theme_mode = ThemeMode.LIGHT
    ph =PermissionHandler()
    page.overlay.append(ph)
    
    def open_app(e):
        ph.open_app_settings()
        
    page.add(
        
        AppBar(
            title=Text("Flash App"),
            color='white',
            bgcolor='#e3113e',
           
            actions=[
                IconButton(Icons.SETTINGS, on_click=open_app)
            ]
        ),
        
        Row([
            Text('\n\n flash light app', size=31, color='black')
        ], alignment='center'
        ),
        Row([
            Image(src="logo.png", width=360, height=360, fit='contain', border_radius=10)
        ], alignment='center'
        ),
        Row([
            ElevatedButton(
                "ON",
                width=100,
                icon=Icons.PLAY_ARROW,
                style=ButtonStyle(
                    bgcolor="#e3113e",
                    color=' white',
                    shape=RoundedRectangleBorder(radius=10),
                    padding=15
                ),
                on_click=...
            ),
            
             ElevatedButton(
                "OFF",
                width=100,
                icon=Icons.PLAY_DISABLED_SHARP,
                style=ButtonStyle(
                    bgcolor="#e3113e",
                    color=' white',
                    shape=RoundedRectangleBorder(radius=10),
                    padding=15
                ),
                on_click=...
            )
        
        
        ],        alignment='center') ,
        Row([
            Text('\n\n @Ibrahim Albukari  2025', size=13, color='black')
        ], alignment='center'
        ),  
    
    )
    page.update()

app(main)