from behave import given, when, then
from pages.login_page import LoginPage  # <-- Tu página de login actual

@given('que el usuario abre la página de inicio de sesión de SauceDemo')
def step_abrir_pagina(context):
    # Behave usa 'context' en vez de 'browser' para pasar el navegador
    context.login_page = LoginPage(context.browser)
    context.login_page.open()

@when('ingresa el usuario "{usuario}" y la contraseña "{contraseña}"')
def step_ingresar_credenciales(context, usuario, contraseña):
    context.login_page.enter_username(usuario)
    context.login_page.enter_password(contraseña)
    context.login_page.click_login()

@then('el sistema lo redirige a la pantalla de inventario')
def step_verificar_home(context):
    # Valido que entré en la app
    assert "inventory.html" in context.browser.current_url

@then('se muestra el mensaje de error "{mensaje}"')
def step_verificar_error(context, mensaje):
    texto_error_visible = context.login_page.get_error_message()
    assert texto_error_visible == mensaje