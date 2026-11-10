import requests
from utils.helpers import logger

def obtener_publicaciones(api_url):
    logger.info(f"Obteniendo publicaciones desde {api_url}")
    respuesta = requests.get(api_url)
    return respuesta

def obtener_publicacion_por_id(api_url, id_publicacion=1):
    logger.info(f"Obteniendo publicación con ID {id_publicacion} desde {api_url}")
    url_completa = f"{api_url}/{id_publicacion}"
    respuesta = requests.get(url_completa)
    return respuesta

def crear_publicacion(api_url, datos):
    logger.info(f"Creando publicación en {api_url} con datos: {datos}")
    respuesta = requests.post(api_url, json=datos)
    return respuesta

def obtener_usuarios(api_url):
    logger.info(f"Obteniendo usuarios desde {api_url}")
    respuesta = requests.get(api_url)
    return respuesta

def obtener_usuario_por_id(api_url, id_usuario=1):
    logger.info(f"Obteniendo usuario con ID {id_usuario} desde {api_url}")
    url_completa = f"{api_url}/{id_usuario}"
    respuesta = requests.get(url_completa)
    return respuesta