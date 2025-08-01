from dash import Dash, html, callback, Input, Output, State, no_update

fondo = 'assets/fondo.mp4'
user_name = 'biscuittp'
avatar = 'assets/avatar.gif'

redes = [
    {"name": "donaciones ❤️", "url": "https://streamlabs.com/biscuittp/tip", "imagen": "assets/imagenes/ekko_jinx.gif", "tipo": "imagen"},
    {"name": "twitch", 'url': 'https://www.twitch.tv/biscuittp', 'imagen': "assets/imagenes/twitch.png", "tipo": "texto"},
    {"name": "facebook", 'url': 'https://www.facebook.com/profile.php?id=61577564854485', 'imagen': "assets/imagenes/facebook.png", "tipo": "texto"},
    {"name": "tiktok", 'url': 'https://www.tiktok.com/@biscuittp', 'imagen': "assets/imagenes/tiktok.png", "tipo": "texto"},
    {"name": "discord", 'url': 'https://discord.com/invite/qxbnXfvYqE', 'imagen': "assets/imagenes/discord.png", "tipo": "texto"},
    {"name": "youtube", 'url': 'https://www.youtube.com/@Biscuittp', 'imagen': "assets/imagenes/youtube.png", "tipo": "texto"},
    {"name": "biscuittp#lan", "url": "https://www.leagueofgraphs.com/es/summoner/lan/Biscuittp-LAN", "imagen": "assets/imagenes/challenger.png", "tipo": "texto"},
]

video_destacado = 'https://www.youtube.com/embed/QX_gzgbY5so?si=_YKnD_ZiIwPt4YVP'

app = Dash(__name__, )
server = app.server 

app.layout = html.Div(
    id='main',
    children=[
        html.Audio(
            src='assets/audio.mp3',
            autoPlay=True,
            controls=True,
            loop=True,
            muted=False,
            id='audio',
        ),
        # Fondo
        html.Video(
            src=fondo,
            id='fondo',
            controls=False,
            autoPlay=True,
            loop=True,
            muted=True,
        ),
        html.Div(
            id='fondo_2',
            children=[
                html.Button(
                '🔊',
                id='button_audio',
                ),
                # Avatar
                html.Img(
                    src=avatar,
                    id='avatar',
                ),
                html.P(
                    user_name.title(),
                    id='user_name',
                ),
                
                # Links
                html.Div(
                    className='contenedor_links',
                    children=[
                        html.A(
                            className='link',
                            target='_blank',
                            href=red['url'],
                            children=[
                                html.Img(
                                    src=red['imagen'],
                                    className='icono',
                                ),
                                html.P(
                                    children=red['name'].title(),
                                    className='url_nombre texto'
                                ) if red['tipo'] == 'texto' else None,
                                html.Div(
                                    ' '
                                ),
                            ]
                        ) 
                        if red['tipo'] == 'texto' else
                        html.A(
                            target='_blank',
                            href=red['url'],
                            className='link_imagen',
                            children=[
                                html.Img(
                                    src=red['imagen'],
                                    className='imagen',
                                ),
                                html.P(
                                    children=red['name'].title(),
                                    className='texto imagen_texto',
                                )
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
                    src='assets/gato.gif',
                ),
                html.P(
                    children='Follow me ❤️',
                    style={'font-size': '30px'}
                )
            ]
        )
    ]
)

@callback(
    Output(component_id='audio', component_property='muted'),
    Output(component_id='button_audio', component_property='children'),
    Input(component_id='button_audio', component_property='n_clicks'),
    State(component_id='audio', component_property='muted'),
)
def controlar_sonido(n_clicks, muted):
    if not n_clicks:
        return False, '🔊'
    
    if muted:
        return False, '🔊'
    elif not muted:
        return True, '🔇'

if __name__ == '__main__':
    app.run_server(debug=True, port=8055)