import pytest
import logging
import utils.logger  
from pages.login_page import LoginPage
# Traigo la función para cargar los datos
from data.leer_datos import cargar_usuarios

# Traigo todos los datos del JSON antes de empezar los tests
datos_usuarios = cargar_usuarios()

def test_login_exitoso(driver):
    """Verifica el login usando los datos reales del JSON"""
    logging.info("--- CREADO: Iniciando prueba de Login Exitoso ---")
    login_page = LoginPage(driver)

    # En vez de escribir "standard_user", lo busco en el JSON
    user_valido = datos_usuarios["usuario_valido"]["usuario"]
    clave_valida = datos_usuarios["usuario_valido"]["clave"]

    logging.info(f"Intentando loguear con el usuario: {user_valido}")
    login_page.login(user_valido, clave_valida)

    url_actual = driver.current_url
    logging.info(f"URL alcanzada tras el login: {url_actual}")
    
    assert "/inventory.html" in url_actual, "Error: No se redirigió al inventario."
    logging.info("FINALIZADO: Redirección al inventario validada con éxito.")

def test_login_password_invalido(driver):
    """Verifica el error de contraseña usando los datos del JSON"""
    logging.info("--- CREADO: Iniciando prueba de Login con Password Inválido ---")
    login_page = LoginPage(driver)

    # Busco los datos incorrectos en el JSON
    user_valido = datos_usuarios["usuario_invalido"]["usuario"]
    clave_falsa = datos_usuarios["usuario_invalido"]["clave"]

    logging.info(f"Intentando loguear usuario {user_valido} con clave incorrecta.")
    login_page.login(user_valido, clave_falsa)

    texto_error = login_page.get_error_password_message()
    error_esperado = "Epic sadface: Username and password do not match any user in this service"
    
    assert error_esperado in texto_error
    logging.info("FINALIZADO: Mensaje de error por password inválido capturado correctamente.")
    
def test_forzar_error_evidencia(driver):
    """Test falso creado a propósito para obligar al sistema a sacar una captura de pantalla"""
    logging.info("--- CREADO: Iniciando prueba de simulación de error para evidencia ---")
    logging.info("Navegando a la página de inicio de SauceDemo...")
    driver.get("https://www.saucedemo.com/")
    
    logging.warning("Ejecutando falla intencional para forzar la captura en el reporte...")
    assert False, "Forzando el error para generar la evidencia en la carpeta y en el HTML"