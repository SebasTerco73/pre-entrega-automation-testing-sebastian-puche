import csv
import json
from pathlib import Path
import pathlib
import logging
from logging.handlers import RotatingFileHandler

RUTA_DATOS = Path(__file__).resolve().parents[1] / "data"
RUTA_CSV = RUTA_DATOS / "usuarios.csv"
RUTA_JSON = RUTA_DATOS / "usuarios.json"

def leer_datos_csv():
    datos = []
    try:
        with open(RUTA_CSV, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, skipinitialspace=True)
            for fila in lector:
                if all(campo in fila for campo in ("usuario", "password", "mensaje_esperado")):
                    datos.append((
                        fila["usuario"],
                        fila["password"],
                        fila["mensaje_esperado"],
                    ))
    except FileNotFoundError as e:
        print(f"Error al leer el archivo CSV: {e}")
    return datos

def leer_datos_json():
    datos = []
    try:
        with open(RUTA_JSON, mode="r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)
            for item in contenido:
                if all(clave in item for clave in ("usuario", "password", "mensaje_esperado")):
                    datos.append((
                        item["usuario"],
                        item["password"],
                        item["mensaje_esperado"],
                    ))
    except FileNotFoundError as e:
        print(f"Error al leer el archivo JSON: {e}")
    return datos


def leer_datos(archivo=None):
    if archivo and str(archivo).lower().endswith(".csv"):
        return leer_datos_csv()

    if archivo and str(archivo).lower().endswith(".json"):
        return leer_datos_json()

    raise ValueError("Debes indicar un archivo con extensión .csv o .json")

# Logs
# Este archivo se encuentra en utils, por eso se sube un nivel para llegar a la raíz.
audit_dir = pathlib.Path(__file__).resolve().parent.parent / "reports" / "logs"
audit_dir.mkdir(parents=True, exist_ok=True)

log_file = audit_dir / "test_log.log"
handler = RotatingFileHandler(
    log_file,
    maxBytes=5 * 1024 * 1024,  # 5 MB
    backupCount=5,
    encoding="utf-8",
)
formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
handler.setFormatter(formatter)

logger = logging.getLogger("talentolab")
logger.setLevel(logging.INFO)
if not any(isinstance(existing_handler, RotatingFileHandler)
           and existing_handler.baseFilename == str(log_file)
           for existing_handler in logger.handlers):
    logger.addHandler(handler)
