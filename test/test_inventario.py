import pytest
from selenium.webdriver.common.by import By
from utils.helpers import login

@pytest.mark.inventario
def test_02_verificar_inventario(driver):
    login(driver)
    page_title = driver.title
    section_title = driver.find_element(By.CLASS_NAME, "title").text
    assert section_title == "Products", f"Error: El título de la página es incorrecto. Se esperaba 'Products' pero se obtuvo '{page_title}'"

@pytest.mark.inventario
def test_03_productos_visibles(driver):
    login(driver)
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "Error: No se encontraron productos visibles en la página de inventario"

@pytest.mark.inventario
def test_04_verificar_producto_y_precio(driver):
    login(driver)
    producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    assert producto == "Sauce Labs Backpack", f"Error: El nombre del producto es incorrecto. Se esperaba 'Sauce Labs Backpack' pero se obtuvo '{producto}'"
    assert precio == "$29.99", f"Error: El precio del producto es incorrecto. Se esperaba '$29.99' pero se obtuvo '{precio}'"

@pytest.mark.inventario
def test_05_validar_interfaz(driver):
    login(driver)
    # Verificar que el logo de la página esté presente
    logo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.is_displayed(), "Error: El logo de la página no está visible"
    
    # Verificar que el menú de navegación esté presente
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed(), "Error: El menú de navegación no está visible"
    
    # Verificar que el carrito de compras esté presente
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    assert carrito.is_displayed(), "Error: El carrito de compras no está visible"

    # Verificar que el filtro de productos esté presente
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro.is_displayed(), "Error: El filtro de productos no está visible"

    # Verificar que los enlaces a redes sociales estén presentes
    redes = driver.find_element(By.CLASS_NAME, "social")
    assert redes.is_displayed(), "Error: Las redes sociales no están visibles"
