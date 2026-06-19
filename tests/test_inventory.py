import pytest
import logging
import utils.logger  
from selenium import webdriver
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
# 1.  Traigo la función para cargar datos
from data.leer_datos import cargar_usuarios

# 2. Traigo los usuarios del JSON
datos_usuarios = cargar_usuarios()

@pytest.fixture
def driver_logged(driver):
    """Fixture que se loguea usando los datos del JSON"""
    logging.info("--- FIXTURE: Iniciando login automático para pruebas de Inventario ---")
    login_page = LoginPage(driver)
    
    # 3. Traigo los datos del JSON
    user = datos_usuarios["usuario_valido"]["usuario"]
    clave = datos_usuarios["usuario_valido"]["clave"]
    
    logging.info(f"Logueando de fondo con usuario: {user}")
    login_page.login(user, clave)
    logging.info("FIXTURE: Login automático exitoso. Retornando InventoryPage.")
    return InventoryPage(driver)

# --- ACÁ EMPIEZAN LAS FUNCIONES DE PRUEBA ---

def test_titulo_de_la_pagina(driver_logged):
    """Verifica que el título de la pestaña del navegador sea el correcto"""
    logging.info("--- CREADO: Iniciando prueba de Título de la Página ---")
    
    titulo = driver_logged.obtener_titulo()
    logging.info(f"Título capturado del navegador: '{titulo}'")
    
    assert titulo == "Swag Labs", "El título de la página no es correcto"
    logging.info("FINALIZADO: Título de la página validado con éxito.")

def test_productos_visibles(driver_logged):
    """Verifica que la tienda tenga los productos cargados en pantalla"""
    logging.info("--- CREADO: Iniciando prueba de Cantidad de Productos Visibles ---")
    
    # Busco los productos con el nombre correcto y cuento cuántos hay
    productos = driver_logged.obtener_productos()
    cantidad = len(productos)
    logging.info(f"Cantidad de productos detectados en pantalla: {cantidad}")
    
    assert cantidad > 0, "No se encontraron productos visibles en la tienda"
    assert cantidad == 6, f"Se esperaban 6 productos pero se encontraron {cantidad}"
    logging.info("FINALIZADO: Presencia y cantidad exacta de 6 productos validada con éxito.")

def test_elementos_interfaz_grafica(driver_logged):
    """Verifica que el menú lateral y el filtro estén visibles en la pantalla"""
    logging.info("--- CREADO: Iniciando prueba de Elementos de Interfaz Gráfica ---")
    
    menu_ok = driver_logged.menu_visible()
    logging.info(f"Verificación de visibilidad del menú lateral: {menu_ok}")
    assert menu_ok, "El menú de tres rayitas no está presente en la página"
    
    filtro_ok = driver_logged.filtro_visible()
    logging.info(f"Verificación de visibilidad del filtro: {filtro_ok}")
    assert filtro_ok, "El filtro de ordenamiento no está presente en la página"
    
    logging.info("FINALIZADO: Menú lateral y filtro de ordenamiento validados con éxito.")