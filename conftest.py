import pytest
from selenium import webdriver
from pages.login_page import LoginPage
# Cargo los datos para conftest 
from data.leer_datos import cargar_usuarios

datos_usuarios = cargar_usuarios()

@pytest.fixture
def driver():
    """Abre el navegador Chrome en incógnito antes del test y lo cierra al terminar"""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new") 
    options.add_argument("--incognito")
    options.add_argument("--disable-infobars")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5) 
    driver.maximize_window()  
    yield driver

    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    """La fixture que necesita  test_carrito.py para arrancar logueado desde el JSON"""
    login_page = LoginPage(driver)
    
    # Recupera las credenciales válidas estructuradas en el archivo de datos JSON
    user = datos_usuarios["usuario_valido"]["usuario"]
    clave = datos_usuarios["usuario_valido"]["clave"]
    
    login_page.login(user, clave)
    return driver
# Configuración de capturas para el reporte HTML
import os
from datetime import datetime

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Saca la foto si falla y la guarda en la estructura interna del test"""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver") or item.funcargs.get("login_in_driver")
        if driver:
            # 1. Guardamos la foto en la carpeta evidencias
            os.makedirs("evidencias", exist_ok=True)
            timestamp = datetime.now().strftime("%H%M%S")
            nombre_foto = f"evidencias/{item.name}_FALLO_{timestamp}.png"
            driver.save_screenshot(nombre_foto)
            
            # 2. Guardamos el Base64 temporalmente dentro del objeto para usarlo en la tabla
            rep.screenshot_base64 = driver.get_screenshot_as_base64()


def pytest_html_results_table_html(report, data):
    # Si el test falló guarda la captura y la agrega al reporte
    if hasattr(report, "screenshot_base64"):
        html_img = f'<div><img src="data:image/png;base64,{report.screenshot_base64}" alt="screenshot" style="width:600px;height:auto; margin-top:10px;"/></div>'
        data.append(html_img)