from behave import given, when, then
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

@given('Estoy en la pagina de Login')
def step_abrir_pagina_login(context):
    context.driver.get("https://www.saucedemo.com/")
    context.login_page = LoginPage(context.driver)

@when('Ingreso el usuario "{usuario}"')
def step_ingresar_usuario(context, usuario):
    context.login_page._completar_usuario(usuario)

@when('Ingreso la contraseña "{contrasena}"')
def step_ingresar_contrasena(context, contrasena):
    context.login_page._completar_clave(contrasena)

@when('Presiono el boton de Login')
def step_hacer_click_login(context):
    context.login_page._hacer_clic_login()

@then('Debo visualizar la pagina de productos')
def step_ver_pagina_productos(context):
    context.inventory_page = InventoryPage(context.driver)
    assert "inventory" in context.driver.current_url, "No se visualiza la página de productos"
    assert context.inventory_page.obtener_logo_content() == "Swag Labs", "El logo no es el esperado"

@then('Debo visualizar un mensaje de error')
def step_ver_mensaje_error(context):
    if context.login_page._esta_error_visible():
        assert context.login_page.obtener_mensaje_error() == "Epic sadface: Username and password do not match any user in this service", "El mensaje de error no es el esperado"
    else:
        assert False, "No se visualiza el mensaje de error"

@when('Ingreso las siguientes credenciales')
def step_ingresar_credenciales(context):
    credenciales = context.table[0]
    credenciales_usuario = credenciales['usuario']
    credenciales_contrasena = credenciales['password']
    context.login_page.login_completo(credenciales_usuario, credenciales_contrasena)
