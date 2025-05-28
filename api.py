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

from fastapi.middleware.cors import CORSMiddleware

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from typing import Optional

load_dotenv()

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse("static/index.html")

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
    url_preview: Optional[str] = None
    url_spotify: str

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
            url_preview=c.url_preview,
            url_spotify=c.url_spotify
        ) for c in canciones
    ]
