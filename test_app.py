import pytest
from app import app as flask_app  # Importa la instancia 'app' de Flask

@pytest.fixture
def client():
    """Configura el cliente de prueba de Flask."""
    with flask_app.test_client() as client:
        yield client

def test_homepage(client):
    """Verifica que la ruta '/' devuelve el contenido esperado."""
    response = client.get('/')
    # 1. Verifica el código de estado HTTP 200 (OK)
    assert response.status_code == 200
    # 2. Verifica que el contenido HTML contenga el texto esperado
    assert b"Practica Entrega Continua: Hola Mundo!" in response.data