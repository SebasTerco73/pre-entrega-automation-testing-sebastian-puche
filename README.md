# Automatización de pruebas con Selenium y Pytest

Proyecto de automatización de pruebas end-to-end para [Sauce Demo](https://www.saucedemo.com/), desarrollado como parte del curso de Automatización QA.

La suite utiliza el patrón Page Object Model (POM) para separar la interacción con la interfaz de usuario de los casos de prueba. Se validan los flujos principales de inicio de sesión, inventario y carrito de compras.

## Alcance de las pruebas

- Inicio de sesión con credenciales válidas, inválidas y usuario bloqueado.
- Inicio de sesión parametrizado para cubrir diferentes combinaciones de credenciales.
- Visualización del inventario y de sus productos.
- Validación del nombre y precio del primer producto.
- Verificación de elementos principales de la interfaz.
- Agregado de productos al carrito.
- Navegación al carrito y validación de los productos agregados.

## Tecnologías y requisitos

- Python 3.12 o compatible.
- Pytest.
- Selenium WebDriver.
- `webdriver-manager`.
- `pytest-html`.
- Google Chrome instalado.

El proyecto configura Chrome en modo headless, por lo que las pruebas se ejecutan sin abrir una ventana del navegador. `webdriver-manager` descarga y administra automáticamente el controlador compatible con Chrome.

## Estructura del proyecto

```text
prelab/
├── conftest.py              # Fixtures de WebDriver, sesión y evidencias
├── datos.py                 # Datos de prueba
├── pytest.ini               # Markers y configuración de Pytest
├── README.md
├── requirements.txt         # Dependencias a instalar
├── pages/                   # Page Objects
│   ├── cart_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── test/                    # Casos de prueba
│   ├── test_carrito.py
│   ├── test_inventario.py
│   └── test_login.py
├── reports/
│   ├── reporte.html         # Reporte generado por pytest-html
│   ├── ejecucion.log       # Log de ejecución
│   ├── assets/              # Recursos del reporte HTML
│   └── screenshots/         # Capturas de pruebas fallidas
└── utils/
```

## Instalación

1. Clonar el repositorio y ubicarse en la carpeta del proyecto:

   ```bash
   git clone https://github.com/SebasTerco73/pre-entrega-automation-testing-sebastian-puche.git
   cd prelab
   ```

2. Crear y activar un entorno virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   En Windows PowerShell, la activación equivalente es:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Instalar las dependencias:

   ```bash
   pip install selenium pytest pytest-html webdriver-manager
   pip install -r requirements.txt
   ```

4. Comprobar la instalación:

   ```bash
   python --version
   pytest --version
   ```

## Ejecución

Ejecutar toda la suite:

```bash
pytest -v
```

La opción `--html=reports/reporte.html --self-contained-html` está configurada en `pytest.ini`, por lo que el reporte HTML se genera automáticamente.

Ejecutar únicamente los casos de una funcionalidad:

```bash
pytest -m login -v
pytest -m inventario -v
pytest -m carrito -v
```

También existe el marker `actual` para seleccionar los casos que se marquen explícitamente con `@pytest.mark.actual`:

```bash
pytest -m actual -v
```

## Fixtures principales

Las fixtures se encuentran en `conftest.py`:

- `driver`: crea un WebDriver de Chrome en modo headless y cierra el navegador al finalizar cada prueba.
- `login_page`: devuelve una instancia de `LoginPage`.
- `user_session`: inicia sesión con el usuario válido y devuelve `InventoryPage`.
- `carrito_con_producto`: agrega el primer producto y devuelve `CartPage`.

Si una prueba falla, se guarda automáticamente una captura en `reports/screenshots/` con el nombre de la prueba.

## Reportes y evidencias

- Reporte HTML: `reports/reporte.html`
- Log de ejecución: `reports/ejecucion.log`
- Capturas de pruebas fallidas: `reports/screenshots/`

El reporte HTML permite consultar el estado, duración y salida de cada caso ejecutado.

## Datos de prueba

El usuario válido utilizado por las fixtures se define en `datos.py`:

```text
Usuario: standard_user
Contraseña: secret_sauce
```

Estas credenciales pertenecen al entorno demo de Sauce Demo y no deben reutilizarse en aplicaciones reales.

## Notas

- Se necesita conexión a internet para acceder a Sauce Demo y para que `webdriver-manager` descargue el controlador cuando sea necesario.
- La ejecución depende de que Google Chrome esté instalado y disponible en el sistema.
- Los selectores y las interacciones con la aplicación están centralizados en los Page Objects para facilitar su mantenimiento.

## Licencia

Proyecto educativo desarrollado con fines de práctica de automatización de pruebas.
