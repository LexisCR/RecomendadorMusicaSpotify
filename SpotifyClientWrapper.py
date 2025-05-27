from models.Cancion import Cancion
import asyncio

class SpotifyClientWrapper:
    def __init__(self, spotipy_client):
        self.client = spotipy_client

    async def obtener_canciones_por_genero(self, genero):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._sync_obtener_canciones, genero)

    def _sync_obtener_canciones(self, genero):
        resultados = self.client.search(q=f"genre:{genero}", type="track", limit=10)
        canciones = resultados['tracks']['items']
        return [
            Cancion(c['name'], c['artists'][0]['name'], genero, c['preview_url'])
            for c in canciones
        ]