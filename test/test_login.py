import pytest
from utils.helpers import login
from selenium.webdriver.common.by import By

pytestmark = pytest.mark.login

def test_01_login_valido(driver):
    login(driver)
    assert "/inventory.html" in driver.current_url, "Error: No se pudo ingresar a /inventory.html"


def test_02_login_invalido(driver):
    login(driver, "standard_user", "wrong_password")
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert error_message == "Epic sadface: Username and password do not match any user in this service", "Error: No se mostró el mensaje de error esperado"

def test_03_login_user_locked(driver):
    login(driver, "locked_out_user", "secret_sauce")
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert error_message == "Epic sadface: Sorry, this user has been locked out.", "Error: No se mostró el mensaje de error esperado"

