import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pytestmark = pytest.mark.carrito

def test_01_agregar_producto_al_carrito(user_session):
        user_session.agregar_primer_producto()
        wait = WebDriverWait(user_session.driver, 5)
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "inventory_item"), "Remove"))
        assert user_session.obtener_texto_primer_boton_producto() == "Remove", "Error: El producto no se agregó correctamente al carrito"

def test_02_verificar_carrito(carrito_con_producto):
    productos_en_carrito = carrito_con_producto.obtener_productos_en_carrito()
    # Verificar que el producto agregado esté presente en la página del carrito
    assert len(productos_en_carrito) > 0, "Error: No se encontraron productos en el carrito después de agregar uno"


def test_03_navegar_carrito(carrito_con_producto):
    # Verificar que la URL sea la correcta para la página del carrito
    assert carrito_con_producto.esta_en_carrito(), "Error: No se pudo navegar a la página del carrito"

def test_04_producto_en_carrito(carrito_con_producto):
    # Verificar que el producto agregado esté presente en la página del carrito
    productos_carrito_nombres = carrito_con_producto.obtener_nombres_productos()
    assert len(productos_carrito_nombres) > 0, "Error: No se encontraron productos en el carrito después de agregar uno"

    # Verificar que el nombre del producto en el carrito sea el mismo que se agregó
    nombre_producto_carrito = productos_carrito_nombres[0]
    assert nombre_producto_carrito == "Sauce Labs Backpack", f"Error: El nombre del producto en el carrito es incorrecto. Se esperaba 'Sauce Labs Backpack' pero se obtuvo '{nombre_producto_carrito}'"