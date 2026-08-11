import requests
import pytest

@pytest.fixture
def base_url():
    return "https://reqres.in/api"

def test_get_users(base_url):
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200
    data = response.json()
    print(data)  # debug ke liye
    assert isinstance(data, dict)  # safe check

def test_get_single_user(base_url):
    response = requests.get(f"{base_url}/users/2")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "data" in data

def test_create_user(base_url):
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(f"{base_url}/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "name" in data
