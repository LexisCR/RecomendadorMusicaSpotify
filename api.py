from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import asyncio
import os
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

from models.Usuario import Usuario
from models.Recomendador import RecomendadorSpotify
from SpotifyClientWrapper import SpotifyClientWrapper
from helpers import obtener_canciones_para_todos

load_dotenv()

app = FastAPI()

sp = Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
))

spotify_wrapper = SpotifyClientWrapper(sp)
recomendador = RecomendadorSpotify(spotify_wrapper)

class UserRequest(BaseModel):
    nombre: str
    generos_favoritos: List[str]

class CancionResponse(BaseModel):
    titulo: str
    artista: str
    genero: str
    url_preview: str = None

@app.post("/recomendar", response_model=List[CancionResponse])
async def recomendar(user: UserRequest):
    if not user.generos_favoritos:
        raise HTTPException(status_code=400, detail="Debe seleccionar al menos un género.")
    usuario = Usuario(user.nombre, user.generos_favoritos)
    resultados = await obtener_canciones_para_todos([usuario], recomendador)
    canciones = resultados[0]
    return [
        CancionResponse(
            titulo=c.titulo,
            artista=c.artista,
            genero=c.genero,
            url_preview=c.url_preview
        ) for c in canciones
    ]
