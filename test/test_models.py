import unittest
import asyncio
from models.Cancion import Cancion
from models.Usuario import Usuario
from models.Recomendador import RecomendadorSpotify
from SpotifyClientWrapper import SpotifyClientWrapper

class DummySpotifyClientWrapper:
    def __init__(self):
        self.called_with = []

    async def obtener_canciones_por_genero(self, genero):
        self.called_with.append(genero)
        return [Cancion(f"Song_{genero}", f"Artist_{genero}", genero, f"url_{genero}", f"urls_{genero}")]

class TestModels(unittest.TestCase):

    def test_cancion_attributes(self):
        c = Cancion("title", "artist", "genre", "url", "urls")
        self.assertEqual(c.titulo, "title")
        self.assertEqual(c.artista, "artist")
        self.assertEqual(c.genero, "genre")
        self.assertEqual(c.url_preview, "url")
        self.assertEqual(c.url_spotify, "urls")

    def test_usuario_attributes(self):
        u = Usuario("name", ["pop", "rock"])
        self.assertEqual(u.nombre, "name")
        self.assertEqual(u.generos_favoritos, ["pop", "rock"])

    def test_recomendador_recomendar_para_usuario(self):
        dummy_wrapper = DummySpotifyClientWrapper()
        recomendador = RecomendadorSpotify(dummy_wrapper)
        usuario = Usuario("testuser", ["pop", "rock"])

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        recomendaciones = loop.run_until_complete(recomendador.recomendar_para_usuario(usuario))
        loop.close()

        self.assertEqual(len(recomendaciones), 2)
        self.assertEqual(dummy_wrapper.called_with, ["pop", "rock"])
        self.assertEqual(recomendaciones[0].genero, "pop")
        self.assertEqual(recomendaciones[1].genero, "rock")

if __name__ == '__main__':
    unittest.main()
