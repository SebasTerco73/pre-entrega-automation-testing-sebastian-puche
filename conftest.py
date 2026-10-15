import pytest
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from datos import USUARIO_VALIDO, PASSWORD_VALIDO


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
    return LoginPage(driver)

@pytest.fixture
def user_session(login_page):
    login_page.abrir().login_completo(
        USUARIO_VALIDO, PASSWORD_VALIDO
        )
    return InventoryPage(login_page.driver)

@pytest.fixture
def carrito_con_producto(user_session):
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
            driver.save_screenshot(str(image_path))
            print(f"\n[SCREENSHOT] Captura guardada en: {image_path}")
