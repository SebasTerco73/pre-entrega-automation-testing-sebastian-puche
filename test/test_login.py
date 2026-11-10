import pytest
# encontrar archivo de datos
from pages.inventory_page import InventoryPage
from data.datos import USUARIO_VALIDO, PASSWORD_VALIDO, login_parametrized
from utils.helpers import leer_datos
from faker import Faker


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

@pytest.mark.parametrize("usuario,password,mensaje_esperado", login_parametrized)
def test_04_login_parametrizado(login_page, usuario, password, mensaje_esperado):
    login_page.abrir().login_completo(usuario, password)

    if mensaje_esperado == "Login exitoso":
        inventory_page = InventoryPage(login_page.driver)
        assert inventory_page.obtener_titulo() == "Products", \
            "Error: No se pudo iniciar sesión con credenciales válidas"
    else:
        error_message = login_page.obtener_mensaje_error()
        assert error_message == mensaje_esperado, \
            "Error: No se mostró el mensaje de error esperado"


@pytest.mark.parametrize(
    "usuario,password,mensaje_esperado",
    leer_datos("usuarios.csv"),
)
def test_05_login_archivos(login_page, usuario, password, mensaje_esperado):
    login_page.abrir().login_completo(usuario, password)

    if mensaje_esperado == "Login exitoso":
        inventory_page = InventoryPage(login_page.driver)
        assert inventory_page.obtener_titulo() == "Products"
    else:
        assert login_page.obtener_mensaje_error() == mensaje_esperado

def test_06_login_faker(login_page):
    fake = Faker('es_ES')

    usuario_falso = fake.user_name()
    password_falso = fake.password()

    print(f"Usuario falso: {usuario_falso}, Password falso: {password_falso}")

    login_page.abrir().login_completo(usuario_falso, password_falso)
    error_message = login_page.obtener_mensaje_error()
    assert error_message == "Epic sadface: Username and password do not match any user in this service"

# pytest -m -s login -v
# -s para que muestre los prints