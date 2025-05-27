# Recomendador de Música con Spotify

## Introducción
Este proyecto es un recomendador de música que utiliza la API de Spotify para sugerir canciones basadas en los géneros favoritos de diferentes usuarios. Cada usuario tiene una lista de géneros preferidos, y el sistema obtiene canciones populares de Spotify para esos géneros, proporcionando recomendaciones personalizadas.

## Estructura del Proyecto

```
.
├── main.py                      # Archivo principal que ejecuta el programa, carga credenciales, crea usuarios y muestra recomendaciones.
├── helpers.py                   # Funciones auxiliares para filtrar canciones, obtener nombres y manejar recomendaciones concurrentes.
├── SpotifyClientWrapper.py      # Wrapper asíncrono para la API de Spotify que obtiene canciones por género.
├── models/                      # Carpeta que contiene las definiciones de las clases del modelo de datos.
│   ├── __init__.py              # Inicializador del paquete models.
│   ├── Cancion.py               # Clase Cancion que representa una canción con título, artista, género y URL de preview.
│   ├── Recomendador.py          # Clase RecomendadorSpotify que maneja la lógica para recomendar canciones a usuarios.
│   └── Usuario.py               # Clase Usuario que representa un usuario con nombre y géneros favoritos.
├── .gitignore                   # Archivos y carpetas ignorados por git.
├── README.md                    # Este archivo de documentación.
```

## Dependencias

- **spotipy**: Librería oficial para interactuar con la API de Spotify.
- **python-dotenv**: Para cargar variables de entorno desde un archivo `.env` (donde se almacenan las credenciales de Spotify).
- **asyncio**: Para manejar llamadas asíncronas y concurrencia en la obtención de canciones.
  
Estas dependencias permiten una integración eficiente con Spotify y un manejo asíncrono de las solicitudes para mejorar el rendimiento.

## Cómo obtener el Client ID y Client Secret de Spotify

1. Ve a [Spotify for Developers Dashboard](https://developer.spotify.com/dashboard/applications).
2. Inicia sesión con tu cuenta de Spotify o crea una si no tienes.
3. Crea una nueva aplicación.
4. En la página de la aplicación, encontrarás el **Client ID** y podrás generar el **Client Secret**.
5. Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```
SPOTIFY_CLIENT_ID=tu_client_id_aqui
SPOTIFY_CLIENT_SECRET=tu_client_secret_aqui
```

Reemplaza `tu_client_id_aqui` y `tu_client_secret_aqui` con los valores obtenidos.

## Ejemplo de uso

El archivo `main.py` contiene un ejemplo de cómo usar el recomendador:

```python
usuarios = [
    Usuario("Ana", ["k-pop", "pop"]),
    Usuario("Luis", ["latin", "rap"]),
    Usuario("Sofía", ["electronic", "dance"]),
]

resultados = asyncio.run(obtener_canciones_para_todos(usuarios, recomendador))
```

Este script crea usuarios con géneros favoritos, obtiene recomendaciones para cada uno.

---

Con esta documentación, cualquier desarrollador podrá entender la estructura del proyecto, instalar las dependencias necesarias, configurar las credenciales de Spotify y ejecutar el recomendador de música.