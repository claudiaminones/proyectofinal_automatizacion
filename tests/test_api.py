import requests
import logging
import utils.logger  
headers = {
    "x-api-key" : "pub_5bca5ffc8772df976fcf8970168a1ad219ad499c472afbba2f27085fa4b4ef7d"
}

def test_login_valido():
    logging.info("--- CREADO: Iniciando prueba de API - Login Válido ---")
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    logging.info("Enviando petición POST a /api/login con credenciales válidas...")
    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)
    logging.info(f"Respuesta recibida. Status Code: {response.status_code}")

    assert response.status_code == 200
    logging.info("FINALIZADO: Login válido en API aprobado correctamente.")

def test_login_sin_password():
    logging.info("--- CREADO: Iniciando prueba de API - Login Sin Password ---")
    body = {
        "email": "eve.holt@reqres.in",
    }

    logging.info("Enviando petición POST a /api/login sin el campo password...")
    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)
    logging.info(f"Respuesta recibida. Status Code: {response.status_code}")

    body_json = response.json()
    assert response.status_code == 400
    assert body_json["error"] == "Missing password"
    logging.info("FINALIZADO: Error 'Missing password' validado con éxito.")

def test_login_sin_email():
    logging.info("--- CREADO: Iniciando prueba de API - Login Sin Email ---")
    body = {
        "password": "cityslicka",
    }

    logging.info("Enviando petición POST a /api/login sin el campo email...")
    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)
    logging.info(f"Respuesta recibida. Status Code: {response.status_code}")

    body_json = response.json()
    assert response.status_code == 400
    assert body_json["error"] == "Missing email or username"
    logging.info("FINALIZADO: Error 'Missing email or username' validado con éxito.")

def test_create_user():
    logging.info("--- CREADO: Iniciando prueba de API - Crear Usuario ---")
    body = {
        "name": "Claudia",
        "email": "claudia.qa@example.com",  
        "password": "QA_automation123*"      
    }

    logging.info(f"Enviando petición POST a /api/users para crear a {body['name']}...")
    response = requests.post("https://reqres.in/api/users", headers=headers, json=body)
    tiempo_rta = response.elapsed.total_seconds()
    logging.info(f"Respuesta recibida. Status Code: {response.status_code} en {tiempo_rta} seg.")

    data = response.json()

    assert response.status_code == 201
    assert body["email"].count("@") == 1
    assert "*" in body["password"]
    assert data["name"] == body["name"]
    assert data["email"] == body["email"]
    assert tiempo_rta < 1

    logging.info("FINALIZADO: Usuario creado de forma exitosa y validaciones conformes.")

def test_delete_user():
    logging.info("--- CREADO: Iniciando prueba de API - Eliminar Usuario ---")
    logging.info("Enviando petición DELETE a /api/users/2...")
    response = requests.delete("https://reqres.in/api/users/2", headers=headers)
    logging.info(f"Respuesta recibida. Status Code: {response.status_code}")

    assert response.status_code == 204
    logging.info("FINALIZADO: Eliminación de usuario validada correctamente.")

def test_get_user():
    logging.info("--- CREADO: Iniciando prueba de API - Obtener Usuario ---")
    logging.info("Enviando petición GET a /api/users/2...")
    response = requests.get("https://reqres.in/api/users/2", headers=headers)
    tiempo_rta = response.elapsed.total_seconds()
    logging.info(f"Respuesta recibida. Status Code: {response.status_code} en {tiempo_rta} seg.")

    assert response.status_code == 200
    assert tiempo_rta < 1, "El tiempo de ejecución tardó más de lo esperado"
    logging.info("FINALIZADO: Datos de usuario obtenidos dentro del tiempo esperado.")