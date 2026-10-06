# Proyecto de automatización de pruebas con Selenium + Pytest

## Propósito del proyecto

Este proyecto tiene como objetivo automatizar la validación del flujo principal de una aplicación web de e-commerce demo (www.saucedemo.com), cubriendo escenarios clave de autenticación, inventario, interfaz y carrito de compras.

Las pruebas están desarrolladas con Python, Selenium y Pytest, y validan que la UI responda correctamente a acciones típicas del usuario, como:

- Inicio de sesión con credenciales válidas e inválidas
- Navegación al inventario
- Visualización de productos y precios
- Validación de elementos de la interfaz
- Agregar productos al carrito
- Navegar y verificar el carrito de compras

## Tecnologías utilizadas

- Python 3.12
- Pytest
- Selenium WebDriver
- WebDriver Manager
- Google Chrome
- pytest-html
- HTML report generation

## Estructura del proyecto

```text
prelab/
├── conftest.py
├── pytest.ini
├── README.md
├── reports/
│   ├── reporte.html
│   ├── ejecucion.log
│   ├── assets/
│   └── screenshots/
├── test/
│   ├── test_login.py
│   ├── test_inventario.py
│   └── test_carrito.py
├── utils/
│   └── helpers.py
└── .venv/
```

## Instalación de dependencias

1. Clonar el repositorio o abrir la carpeta del proyecto.
2. Crear un entorno virtual:

```bash
python3 -m venv .venv
```

3. Activar el entorno virtual (linux):

```bash
source .venv/bin/activate
```

4. Instalar las dependencias necesarias:

```bash
pip install selenium pytest pytest-html webdriver-manager
```

Si se desea confirmar la instalación:

```bash
python -V
pytest --version
```

## Comandos para ejecutar las pruebas

Ejecutar toda la suite de pruebas con generación de reporte HTML automatico:

```bash
pytest -v 
```

También se puede ejecutar por etiquetas (markers) definidas en `pytest.ini`:

```bash
pytest -m login -v
pytest -m inventario -v
pytest -m carrito -v
```

## Reporte HTML generado por Pytest

El proyecto genera el reporte ejecutable en la siguiente ruta:

- `reports/reporte.html`

Además, el archivo HTML incluye assets y estilos asociados en:

- `reports/assets/`

Este reporte permite revisar de forma visual el resultado de cada prueba, tiempos de ejecución y estado general.

### Capturas de pantalla

Las capturas de pantalla se almacenan en:

- `reports/screenshots/`

Ejemplos de evidencia generada:

- `reports/screenshots/salida_consola.png`
- `reports/screenshots/reporte.png`


### Logs de ejecución

La salida de la ejecución se registra en:

- `reports/ejecucion.log`

Este archivo guarda el resultado detallado de la ejecución de Pytest, incluyendo errores y resumen final.

## Ejecución reciente y resultados observados

Se ejecutó la suite completa del proyecto con el comando indicado. El resultado real de la última ejecución fue:

- 11 pruebas ejecutadas
- 11 pruebas aprobadas
- 0 pruebas fallidas

## Recomendaciones

- Mantener la app en un entorno estable antes de ejecutar pruebas automatizadas.
- Revisar periódicamente el reporte HTML para analizar regresiones.
- Validar la estabilidad de los selectores de la UI cuando la aplicación cambie.

## Licencia

Este proyecto se entrega con fines de práctica y automatización de pruebas dentro del curso de Automatización QA.
