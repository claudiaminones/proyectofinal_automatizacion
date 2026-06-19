import json
import os

def cargar_usuarios():
    """Abre el archivo JSON y le devuelve los datos a los tests"""
    # Obtiene la ruta del directorio actual donde se encuentra este archivo
    ruta_actual = os.path.dirname(__file__)
    ruta_json = os.path.join(ruta_actual, "usuarios.json")
    
    # Abro el archivo y lo transformo en un diccionario de Python
    with open(ruta_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    
    return datos