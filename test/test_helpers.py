import unittest
from helpers import filtrar_canciones_por_popularidad, obtener_nombres_canciones, contar_total_popularidad
from models.Cancion import Cancion

class TestHelpers(unittest.TestCase):

    def setUp(self):
        self.canciones = [
            Cancion("Cancion1", "Artista1", "pop", "url1", "urls1"),
            Cancion("Cancion2", "Artista2", "rock", "url2", "urls2"),
            Cancion("Cancion3", "Artista3", "pop", "url3", "urls3"),
        ]
        self.canciones[0].popularidad = 50
        self.canciones[1].popularidad = 30
        self.canciones[2].popularidad = 70

    def test_filtrar_canciones_por_popularidad(self):
        resultado = filtrar_canciones_por_popularidad(self.canciones, 40)
        self.assertEqual(len(resultado), 2)
        self.assertIn(self.canciones[0], resultado)
        self.assertIn(self.canciones[2], resultado)

    def test_obtener_nombres_canciones(self):
        resultado = obtener_nombres_canciones(self.canciones)
        self.assertEqual(resultado, ["Cancion1", "Cancion2", "Cancion3"])

    def test_contar_total_popularidad(self):
        resultado = contar_total_popularidad(self.canciones)
        self.assertEqual(resultado, 150)

if __name__ == '__main__':
    unittest.main()
