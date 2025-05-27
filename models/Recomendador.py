class RecomendadorSpotify:
    def __init__(self, spotify_client):
        self.spotify_client = spotify_client

    async def recomendar_para_usuario(self, usuario):
        recomendaciones = []
        for genero in usuario.generos_favoritos:
            canciones = await self.spotify_client.obtener_canciones_por_genero(genero)
            recomendaciones.extend(canciones)
        return recomendaciones