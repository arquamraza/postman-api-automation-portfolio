import pytest
import requests

def test_create_user():
    url = "https://jsonplaceholder.typicode.com/users"
    payload = {
        "name" : "Arquam Raza Updated",
        "email" : "arquam.update@gmail.com",
        "username" : "arquam_sdet"
    }
    response = requests.post(url, json=payload)
    print(response.json())
    assert response.status_code == 201
    assert response.json()["name"] == "Arquam Raza Updated"
def test_update_user():
    url = "https://jsonplaceholder.typicode.com/users/1"
    payload = {
        "name": "Arquam Raza PUT Done",
        "email": "arquam.put@gmail.com"
    }
    response = requests.put(url, json=payload)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["name"] == "Arquam Raza PUT Done"

def test_delete_user():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.delete(url)
    print(f"Delete status: {response.status_code}")
    assert response.status_code == 200