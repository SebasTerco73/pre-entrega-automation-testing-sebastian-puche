import base64

import pytest
from pathlib import Path
import pytest_html

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from data.datos import USUARIO_VALIDO, PASSWORD_VALIDO

from utils.helpers import logger


@pytest.fixture(scope="function")
def driver():
    reports_dir = Path(__file__).resolve().parent / "reports"
    screenshots_dir = reports_dir / "screenshots"
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    options = Options()
    options.add_argument("--headless=new") # Usar el nuevo modo headless de Chrome hace que las pruebas sean más rápidas y no abran una ventana del navegador.
    options.add_argument("--window-size=1920,1080") # Establece un tamaño de ventana fijo para evitar problemas de visualización en modo headless.
    options.add_argument("--disable-gpu") # Deshabilita la aceleración por hardware para evitar problemas en algunos entornos.
    options.add_argument("--no-sandbox") # Deshabilita el sandbox de Chrome, necesario en algunos entornos de CI/CD.
    options.add_argument("--disable-dev-shm-usage") # Evita problemas de espacio compartido en contenedores Docker.

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    driver.implicitly_wait(2) 
    yield driver

    driver.quit()

@pytest.fixture
def login_page(driver):
    logger.info("Abriendo la página de login")
    return LoginPage(driver)

@pytest.fixture
def user_session(login_page):
    logger.info("Iniciando sesión con usuario válido")
    login_page.abrir().login_completo(
        USUARIO_VALIDO, PASSWORD_VALIDO
        )
    return InventoryPage(login_page.driver)

@pytest.fixture
def carrito_con_producto(user_session):
    logger.info("Agregando un producto al carrito")
    user_session.agregar_primer_producto()

    user_session.esperar_boton_remove()

    cart_page = user_session.ir_al_carrito()
    return cart_page


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            screenshots_dir = Path(__file__).resolve().parent / "reports" / "screenshots"
            screenshots_dir.mkdir(parents=True, exist_ok=True)
            image_path = screenshots_dir / f"{item.name}.png"
            captura = driver.save_screenshot(str(image_path))
            if captura:
                print(f"\n[SCREENSHOT] Captura guardada en: {image_path}")

                imagen_base64 = base64.b64encode(
                    image_path.read_bytes()
                ).decode("utf-8")

                extras = getattr(report, "extras", [])
                extras.append(
                    pytest_html.extras.image(
                        imagen_base64,
                        mime_type="image/png",
                        extension="png",
                        name="Captura de error",
                    )
                )
                report.extras = extras

def pytest_html_report_title(report):
    report.title = "Reporte de Pruebas Automatizadas - Sauce Demo"
