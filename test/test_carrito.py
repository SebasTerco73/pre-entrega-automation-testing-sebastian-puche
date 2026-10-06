import pytest
from selenium.webdriver.common.by import By
from utils.helpers import login,ir_al_carrito, agregar_producto_al_carrito
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pytestmark = pytest.mark.carrito

def test_06_agregar_producto_al_carrito(driver):
        login(driver)
        # Obtener el primer elemento de la lista de productos, tira error
        agregar_producto_al_carrito(driver)
        wait = WebDriverWait(driver, 5)
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "inventory_item"), "Remove"))
        first_item = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
        boton_remove = first_item.find_element(By.TAG_NAME, "button")
        assert boton_remove.text.capitalize() == "Remove", "Error: El botón no cambió a 'Remove' después de agregar el producto al carrito"

def test_07_verificar_carrito(driver):
    login(driver)
    agregar_producto_al_carrito(driver)
    wait = WebDriverWait(driver, 5)
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "inventory_item"), "Remove"))
    ir_al_carrito(driver)
    # Verificar que el producto agregado esté presente en la página del carrito
    productos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(productos_carrito) > 0, "Error: No se encontraron productos en el carrito después de agregar uno"


def test_08_navegar_carrito(driver):
    login(driver)
    ir_al_carrito(driver)
    # Verificar que la URL sea la correcta para la página del carrito
    assert "/cart.html" in driver.current_url, "Error: No se pudo navegar a la página del carrito"


def test_09_producto_en_carrito(driver):
    login(driver)
    agregar_producto_al_carrito(driver)
    ir_al_carrito(driver)
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))

    # Verificar que el producto agregado esté presente en la página del carrito
    productos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(productos_carrito) > 0, "Error: No se encontraron productos en el carrito después de agregar uno"
    
    # Verificar que el nombre del producto en el carrito sea el mismo que se agregó
    nombre_producto_carrito = productos_carrito[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombre_producto_carrito == "Sauce Labs Backpack", f"Error: El nombre del producto en el carrito es incorrecto. Se esperaba 'Sauce Labs Backpack' pero se obtuvo '{nombre_producto_carrito}'"