import json
import os
from datetime import datetime

import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_FILE = os.path.join(BASE_DIR, "data", "cache_tasas.json")
URL_DOLAR = "https://ve.dolarapi.com/v1/dolares/oficial"
URL_EURO = "https://ve.dolarapi.com/v1/euros/oficial"
MAX_REGISTROS = 10


def leer_cache():
    """Devuelve el historial guardado, o {} si no existe o está dañado."""
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def guardar_tasas(tasa_dolar, tasa_euro):
    """Guarda las tasas con la hora actual y conserva solo las últimas 10."""
    historial = leer_cache()
    hora = datetime.now().strftime("%Y-%m-%d %H:%M")
    historial[hora] = {"dolar": tasa_dolar, "euro": tasa_euro}

    while len(historial) > MAX_REGISTROS:
        del historial[list(historial.keys())[0]]

    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as archivo:
        json.dump(historial, archivo, indent=4)


def obtener_tasa_con_respaldo(url, moneda):
    """Pide la tasa a la API; si falla, usa la última guardada en el cache."""
    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        return float(respuesta.json()["promedio"])
    except (requests.exceptions.RequestException, KeyError, ValueError, TypeError):
        print(f"No se pudo consultar la tasa del {moneda}. Usando la última guardada.")

    historial = leer_cache()
    if historial:
        ultima_fecha = list(historial.keys())[-1]
        return float(historial[ultima_fecha][moneda])
    return 0.0


def tasa_dia():
    """Devuelve {'dolar': ..., 'euro': ...} y actualiza el cache si hubo datos."""
    tasa_dolar = obtener_tasa_con_respaldo(URL_DOLAR, "dolar")
    tasa_euro = obtener_tasa_con_respaldo(URL_EURO, "euro")

    if tasa_dolar > 0 and tasa_euro > 0:
        guardar_tasas(tasa_dolar, tasa_euro)

    return {"dolar": tasa_dolar, "euro": tasa_euro}
