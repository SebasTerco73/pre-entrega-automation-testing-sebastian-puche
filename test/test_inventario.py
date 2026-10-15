import pytest
from selenium.webdriver.common.by import By

pytestmark = pytest.mark.inventario

def test_02_verificar_inventario(user_session):
    section_title = user_session.obtener_titulo()
    assert section_title == "Products", f"Error: El título de la página es incorrecto. Se esperaba 'Products' pero se obtuvo '{section_title}'"

def test_03_productos_visibles(user_session):
    productos = user_session.obtener_productos()
    assert len(productos) > 0, "Error: No se encontraron productos visibles en la página de inventario"

def test_04_verificar_producto_y_precio(user_session):
    user_session = user_session.agregar_primer_producto()
    producto = user_session.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = user_session.driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    assert producto == "Sauce Labs Backpack", f"Error: El nombre del producto es incorrecto. Se esperaba 'Sauce Labs Backpack' pero se obtuvo '{producto}'"
    assert precio == "$29.99", f"Error: El precio del producto es incorrecto. Se esperaba '$29.99' pero se obtuvo '{precio}'"

@pytest.mark.parametrize("selector, nombre", [
    ((By.CLASS_NAME, "app_logo"), "logo de la pagina"),
    ((By.ID, "react-burger-menu-btn"), "menú de navegacion"),
    ((By.CLASS_NAME, "shopping_cart_link"), "carrito de compras"),
    ((By.CLASS_NAME, "product_sort_container"), "filtro de productos"),
    ((By.CLASS_NAME, "social"), "redes sociales")
])
def test_05_validar_interfaz(user_session, selector, nombre):
    # Verificar que el elemento esté presente
    assert user_session.elemento_esta_visible(selector), (
            f"Error: {nombre} no está visible"
    )

    
 
