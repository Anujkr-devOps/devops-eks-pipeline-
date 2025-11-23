import sys
sys.path.append('app')
from app import app
def test_hello_world():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World From DevOps AKS Pipeline! from AKS Pods for Video Demo'