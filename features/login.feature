@ui
Feature: Autenticación en SauceDemo

  Background:
    Dado que el usuario abre la página de inicio de sesión de SauceDemo

  @smoke
  Scenario: Inicio de sesión exitoso con credenciales válidas
    Cuando ingresa el usuario "standard_user" y la contraseña "secret_sauce"
    Entonces el sistema lo redirige a la pantalla de inventario

  Scenario Outline: Intento de inicio de sesión fallido con credenciales incorrectas
    Cuando ingresa el usuario "<usuario>" y la contraseña "<contraseña>"
    Entonces se muestra el mensaje de error "<mensaje>"

    Examples:
      | usuario         | contraseña      | mensaje                                                     |
      | locked_out_user | secret_sauce    | Epic sadface: Sorry, this user has been locked out.          |
      | usuario_invalido| clave_incorrecta | Epic sadface: Username and password do not match any user... |
      |                 | secret_sauce    | Epic sadface: Username is required                           |