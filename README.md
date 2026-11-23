# Automatización de pruebas con Selenium, Pytest y Behave

Proyecto de automatización de pruebas end-to-end para [Sauce Demo](https://www.saucedemo.com/), desarrollado como parte del curso de Automatización QA.

La suite combina:

- Pruebas tradicionales con **Pytest** y el patrón Page Object Model (POM).
- Pruebas de comportamiento escritas en lenguaje Gherkin con **Behave**.

## Alcance de las pruebas

- Inicio de sesión con credenciales válidas e inválidas.
- Inicio de sesión parametrizado y por tabla de datos.
- Visualización del inventario y de sus productos.
- Validación del nombre y precio del primer producto.
- Verificación de elementos principales de la interfaz.
- Agregado de productos al carrito y navegación al carrito.

## Tecnologías y requisitos

- Python 3.12 o compatible.
- Google Chrome instalado.
- Selenium WebDriver.
- Pytest y pytest-html.
- Behave para escenarios Gherkin.
- Webdriver-manager para administrar el controlador de Chrome.
- Faker y pytest-check como utilidades de pruebas.

El proyecto configura Chrome en modo headless, por lo que las pruebas se ejecutan sin abrir una ventana del navegador. `webdriver-manager` descarga y administra automáticamente el controlador compatible con Chrome.

## Dependencias (`requirements.txt`)

Las dependencias del proyecto se mantienen centralizadas en `requirements.txt`:

```text
behave
selenium
pytest
pytest-html
webdriver-manager
faker
pytest-check
```

Cambios recientes documentados:

- Se agregó **`behave`** para ejecutar las pruebas escritas en Gherkin.
- Se agregó/correctamente declaró **`pytest-check`** para utilizar aserciones adicionales de Pytest. Antes figuraba `pitest-check`, un nombre incorrecto.
- Se conservaron las dependencias necesarias para Selenium, Pytest, reportes HTML, manejo del ChromeDriver y generación de datos de prueba.

## Estructura del proyecto

```text
prelab/
├── conftest.py              # Fixtures y evidencias de Pytest
├── pytest.ini               # Markers y configuración de Pytest
├── requirements.txt         # Dependencias del proyecto
├── README.md
├── data/
│   ├── datos.py             # Datos de prueba
│   ├── usuarios.csv
│   └── usuarios.json
├── features/                # Pruebas de Behave
│   ├── login.feature
│   ├── cart.feature
│   ├── environment.py       # Hooks y configuración de WebDriver
│   └── steps/
│       └── login_step.py
├── pages/                   # Page Objects
│   ├── cart_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── test/                    # Casos de prueba de Pytest
│   ├── test_carrito.py
│   ├── test_inventario.py
│   └── test_login.py
├── reports/
│   ├── reporte.html         # Reporte generado por pytest-html
│   ├── ejecucion.log        # Log de ejecución
│   ├── assets/
│   └── screenshots/         # Capturas de pruebas fallidas
└── utils/
```

## Instalación

1. Clonar el repositorio y ubicarse en la carpeta del proyecto:

   ```bash
   git clone https://github.com/SebasTerco73/pre-entrega-automation-testing-sebastian-puche.git
   cd pre-entrega-automation-testing-sebastian-puche
   ```

2. Crear y activar un entorno virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   En Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Instalar todas las dependencias:

   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

4. Comprobar la instalación:

   ```bash
   python --version
   pytest --version
   behave --version
   ```

## Ejecución con Pytest

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

Ejecutar explícitamente los casos marcados con `@pytest.mark.actual`:

```bash
pytest -m actual -v
```

## Ejecución con Behave

Desde la raíz del proyecto, ejecutar todos los escenarios Gherkin:

```bash
behave
```

Para mostrar más detalle:

```bash
behave -v
```

### Ejecutar Behave por tags

Los tags permiten ejecutar escenarios seleccionados. Los tags disponibles actualmente incluyen:

- `@login`: Feature completa de inicio de sesión.
- `@smoke`: Escenario de login exitoso.
- `@regression`: Escenario de login con usuario incorrecto.

Ejecutar todos los escenarios del feature `login`:

```bash
behave --tags=@login
```

Ejecutar únicamente las pruebas marcadas como smoke:

```bash
behave --tags=@smoke
```

Ejecutar únicamente las pruebas marcadas como regression:

```bash
behave --tags=@regression
```

Puede combinarse el criterio de tags:

```bash
behave --tags="@login and @smoke"
behave --tags="@login and not @regression"
```

Los archivos Gherkin se encuentran en `features/` y sus definiciones de pasos en `features/steps/`. El hook `features/environment.py` crea y finaliza el navegador para cada escenario.

## Fixtures principales de Pytest

Las fixtures se encuentran en `conftest.py`:

- `driver`: crea un WebDriver de Chrome en modo headless y cierra el navegador al finalizar cada prueba.
- `login_page`: devuelve una instancia de `LoginPage`.
- `user_session`: inicia sesión con el usuario válido y devuelve `InventoryPage`.
- `carrito_con_producto`: agrega el primer producto y devuelve `CartPage`.

Si una prueba de Pytest falla, se guarda automáticamente una captura en `reports/screenshots/` con el nombre de la prueba.

## Reportes y evidencias

- Reporte HTML de Pytest: `reports/reporte.html`
- Log de ejecución: `reports/ejecucion.log`
- Capturas de pruebas fallidas: `reports/screenshots/`

El reporte HTML permite consultar el estado, duración y salida de cada caso ejecutado.

## Datos de prueba

El usuario válido utilizado por las fixtures y los escenarios se define en `data/datos.py`:

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
