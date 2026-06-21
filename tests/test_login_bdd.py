from pytest_bdd import scenario, given, when, then
import pytest


@scenario('../features/login.feature', 'Inicio de sesión exitoso con credenciales válidas')
def test_login_exitoso():
    pass

@scenario('../features/login.feature', 'Intento de inicio de sesión fallido con credenciales incorrectas')
def test_login_fallido():
    pass

