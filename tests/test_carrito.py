import pytest
import logging
import utils.logger  
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

def test_agregar_producto_al_carrito(login_in_driver):
    """Prueba que un producto se agregue correctamente al carrito"""
    logging.info("--- CREADO: Iniciando prueba de Agregar Producto al Carrito ---")
    driver = login_in_driver

    # 1. Dejo lista la página de productos
    inventario = InventoryPage(driver)

    # 2. Agrego el primer producto al carrito 
    logging.info("Intentando agregar el primer producto al carrito...")
    inventario.agregar_producto_al_carrito()

    # 3. Verifico que el contador del carrito se actualice a 1
    logging.info("Validando el estado del contador del carrito...")
    contador = inventario.obtener_contador_carrito()
    logging.info(f"Contador del carrito detectado: '{contador}'")
    
    assert contador == "1", f"Error: Se esperaba '1' en el carrito pero se obtuvo '{contador}'"
    logging.info("FINALIZADO: Producto agregado y contador validado con éxito.")