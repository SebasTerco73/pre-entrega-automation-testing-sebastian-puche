import pytest
from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage
from datos import USUARIO_VALIDO, PASSWORD_VALIDO

pytestmark = pytest.mark.login

credenciales = {
    "valido": (USUARIO_VALIDO, PASSWORD_VALIDO),
    "invalido": (USUARIO_VALIDO, "wrong_password"),
    "bloqueado": ("locked_out_user", PASSWORD_VALIDO)
}

def test_01_login_valido(login_page):
    user, password = credenciales["valido"]
    login_page.abrir().login_completo(user, password)
    inventory_page = InventoryPage(login_page.driver)
    assert inventory_page.obtener_titulo() == "Products", "Error: No se pudo iniciar sesión con credenciales válidas"

def test_02_login_invalido(login_page):
    user, password = credenciales["invalido"]
    login_page.abrir().login_completo(user, password)
    error_message = login_page.obtener_mensaje_error()
    assert error_message == "Epic sadface: Username and password do not match any user in this service", "Error: No se mostró el mensaje de error esperado para login inválido"

def test_03_login_user_locked(login_page):
    user, password = credenciales["bloqueado"]
    login_page.abrir().login_completo(user, password)
    error_message = login_page.obtener_mensaje_error()
    assert error_message == "Epic sadface: Sorry, this user has been locked out.", "Error: No se mostró el mensaje de error esperado"

@pytest.mark.parametrize("usuario,password,deberia_funcionar", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("standard_user", "wrong_password", False),
])
def test_04_login_parametrizado(login_page, usuario, password, deberia_funcionar):
    login_page.abrir().login_completo(usuario, password)
    if deberia_funcionar:
        inventory_page = InventoryPage(login_page.driver)
        assert inventory_page.obtener_titulo() == "Products", "Error: No se pudo iniciar sesión con credenciales válidas"
    else:
        error_message = login_page.obtener_mensaje_error()
        assert error_message == "Epic sadface: Sorry, this user has been locked out." or error_message == "Epic sadface: Username and password do not match any user in this service", "Error: No se mostró el mensaje de error esperado"