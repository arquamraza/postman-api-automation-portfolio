import requests
import pytest

@pytest.fixture
def base_url():
    return "https://reqres.in/api"

def test_get_users(base_url):
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0

def test_get_single_user(base_url):
    response = requests.get(f"{base_url}/users/2")
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == 2

def test_create_user(base_url):
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(f"{base_url}/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "morpheus"
