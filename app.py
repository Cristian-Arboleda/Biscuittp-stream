from dash import Dash, html, dcc

app = Dash()

user_name = 'biscuittp'

redes = [
    {"name": "twitch", 'url': 'https://www.twitch.tv/biscuittp', 'icono': "assets/iconos/twitch.png", "tipo": "texto"},
    {"name": "facebook", 'url': 'https://www.facebook.com/profile.php?id=61577564854485', 'icono': "assets/iconos/facebook.png", "tipo": "texto"},
    {"name": "tiktok", 'url': 'https://www.twitch.tv/biscuittp', 'icono': "assets/iconos/tiktok.png", "tipo": "texto"},
    {"name": "discord", 'url': 'https://discord.com/invite/qxbnXfvYqE', 'icono': "assets/iconos/discord.png", "tipo": "texto"},
    {"name": "youtube", 'url': 'https://www.youtube.com/@Biscuittp', 'icono': "assets/iconos/youtube.png", "tipo": "texto"},
    {"name": "donaciones", "url": "https://streamlabs.com/biscuittp/tip", "icono": "assets/iconos/donacion.png", "tipo": "imagen"},
    {"name": "biscuittp#lan", "url": "https://www.leagueofgraphs.com/es/summoner/lan/Biscuittp-LAN", "icono": "assets/iconos/challenger.png", "tipo": "texto"},
]

video_destacado = 'https://www.youtube.com/embed/QX_gzgbY5so?si=_YKnD_ZiIwPt4YVP'


app.layout = html.Div(
    id='main',
    # Fondo
    children=[
        html.Video(
            src='assets/fondo.mp4',
            id='fondo',
            controls=False,
            autoPlay=True,
            loop=True,
            muted=True,
        ),
        html.Div(
            id='fondo_2',
            children=[
                html.Img(
                    src='assets/avatar.gif',
                    id='avatar',
                ),
                html.P(
                    user_name.title(),
                    id='user_name',
                ),
                html.Div(
                    className='contenedor_links',
                    children=[
                        html.A(
                            className='link',
                            target='_blank',
                            href=red['url'],
                            children=[
                                html.Img(
                                    src=red['icono'],
                                    className='icono',
                                ),
                                html.P(
                                    children=red['name'].title(),
                                    className='url_nombre'
                                ),
                                html.Div(
                                    ' '
                                ),
                            ]
                        )
                        for red in redes
                    ]
                ),
                html.Iframe(
                    src=video_destacado,
                    id='video_destacado',
                ),
                html.Img(
                    src='assets/gato.gif'
                ),
                html.P(
                    children='Followme ❤️',
                    style={'font-size': '30px'}
                )
            ]
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True, port=8055)