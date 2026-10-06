from selenium.webdriver.common.by import By

BASE_URL = "https://www.saucedemo.com/"
USUARIO_VALIDO = "standard_user"
PASSWORD_VALIDO = "secret_sauce"


def login(driver, username=USUARIO_VALIDO, secret=PASSWORD_VALIDO):
    driver.get(BASE_URL)
    assert "Swag Labs" in driver.title

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(secret)
    driver.find_element(By.ID, "login-button").click()


def agregar_producto_al_carrito(driver):
    first_item = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    boton_agregar = first_item.find_element(By.TAG_NAME, "button")
    boton_agregar.click()


def ir_al_carrito(driver):
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    carrito.click()
