import unittest
from unittest.mock import MagicMock, patch
import asyncio
from SpotifyClientWrapper import SpotifyClientWrapper
from models.Cancion import Cancion

class TestSpotifyClientWrapper(unittest.TestCase):

    def setUp(self):
        self.mock_spotify_client = MagicMock()
        self.wrapper = SpotifyClientWrapper(self.mock_spotify_client)

    def test_sync_obtener_canciones(self):
        self.mock_spotify_client.search.return_value = {
            'tracks': {
                'items': [
                    {
                        'name': 'Song1',
                        'artists': [{'name': 'Artist1'}],
                        'preview_url': 'url1'
                    },
                    {
                        'name': 'Song2',
                        'artists': [{'name': 'Artist2'}],
                        'preview_url': 'url2'
                    }
                ]
            }
        }
        canciones = self.wrapper._sync_obtener_canciones('pop')
        self.assertEqual(len(canciones), 2)
        self.assertIsInstance(canciones[0], Cancion)
        self.assertEqual(canciones[0].titulo, 'Song1')
        self.assertEqual(canciones[0].artista, 'Artist1')
        self.assertEqual(canciones[0].genero, 'pop')
        self.assertEqual(canciones[0].url_preview, 'url1')

    def test_obtener_canciones_por_genero(self):
        async def run_test():
            canciones = await self.wrapper.obtener_canciones_por_genero('pop')
            self.assertIsInstance(canciones, list)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(run_test())
        loop.close()

if __name__ == '__main__':
    unittest.main()
