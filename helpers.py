from functools import reduce

def filtrar_canciones_por_popularidad(canciones, umbral):
    return list(filter(lambda c: c.popularidad >= umbral, canciones))

def obtener_nombres_canciones(canciones):
    return list(map(lambda c: c.titulo, canciones))

def contar_total_popularidad(canciones):
    return reduce(lambda acc, c: acc + getattr(c, 'popularidad', 0), canciones, 0)

import asyncio

async def obtener_canciones_para_todos(usuarios, recomendador):
    tareas = [recomendador.recomendar_para_usuario(u) for u in usuarios]
    return await asyncio.gather(*tareas)
