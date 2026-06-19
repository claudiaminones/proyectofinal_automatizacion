# Proyecto de Automatización QA - Claudia Miñones

## Descripción

Proyecto de automatización de pruebas de extremo a extremo (End-to-End) realizado con Python, Selenium WebDriver y Pytest. 

El objetivo es evaluar de forma dinámica la interfaz de usuario de la plataforma SauceDemo utilizando el patrón de diseño Page Object Model (POM) y Data-Driven Testing, además de validar servicios mediante pruebas de API.

## Tecnologías usadas
- Python 3.12
- Selenium WebDriver
- Pytest
- Requests (Pruebas de API)

## Estructura del Proyecto
- `data/`: Contiene el archivo `usuarios.json` con los escenarios de prueba y el script `leer_datos.py`.
- `pages/`: Clases bajo el patrón POM (`login_page.py` e `inventory_page.py`).
- `tests/`: Batería con las 12 pruebas automatizadas (`test_login.py`, `test_inventory.py`, `test_carrito.py` y `test_api.py`).

## Instalación de dependencias

Para instalar las librerías necesarias, ejecutar en la terminal:
`pip install -r requirements.txt`

## Funcionamiento de las pruebas

Para ejecutar la suite completa de 12 pruebas (UI + API) con el reporte detallado, ingresar el siguiente comando:
`pytest -v`