import csv
import json
from pathlib import Path
import pathlib
import logging

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
# Quiero que vaya en la raiz/reports/logs/test_log.log, teniendo en cuenta que este archivo helpers.py está en utils/, por lo que debo subir 1 nivel para llegar a la raíz del proyecto.
audit_dir = pathlib.Path(__file__).resolve().parent.parent / "reports" / "logs"
audit_dir.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    filename=audit_dir / "test_log.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("talentolab")
