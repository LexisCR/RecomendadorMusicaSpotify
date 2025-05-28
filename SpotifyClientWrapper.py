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
        canciones = resultados.get('tracks', {}).get('items', [])
        lista_canciones = []
        for c in canciones:
            url_spotify = c.get('external_urls', {}).get('spotify', None)
            cancion = Cancion(
                c.get('name', 'Desconocido'),
                c.get('artists', [{}])[0].get('name', 'Desconocido'),
                genero,
                c.get('preview_url', None),
                url_spotify
            )
            lista_canciones.append(cancion)
        return lista_canciones