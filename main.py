import asyncio
import os
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

from models.Usuario import Usuario
from models.Recomendador import RecomendadorSpotify
from SpotifyClientWrapper import SpotifyClientWrapper
from helpers import obtener_canciones_para_todos

# Cargar credenciales
load_dotenv()

sp = Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
))

spotify_wrapper = SpotifyClientWrapper(sp)
recomendador = RecomendadorSpotify(spotify_wrapper)

usuarios = [
    Usuario("Ana", ["k-pop", "pop"]),
    Usuario("Luis", ["latin", "rap"]),
    Usuario("Sofía", ["electronic", "dance"]),
]

resultados = asyncio.run(obtener_canciones_para_todos(usuarios, recomendador))

for usuario, canciones in zip(usuarios, resultados):
    print(f"\n🎧 Recomendaciones para {usuario.nombre}:")
    for cancion in canciones:
        print(f" - {cancion.titulo} de {cancion.artista}")