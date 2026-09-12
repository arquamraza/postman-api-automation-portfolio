import requests

def test_get_user_list(base_url, headers):
    """Check if we can get list of users"""
    response = requests.get(f"{base_url}/users", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) > 0  # list aati hai yaha

def test_get_single_user(base_url, headers):
    """Check if we can get single user"""
    response = requests.get(f"{base_url}/users/1", headers=headers)  # id 1
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_create_user(base_url, headers):
    """Check if we can create user"""
    payload = {
        "name": "Arquam",
        "username": "arquam_sdet",
        "email": "arquam@test.com"
    }
    response = requests.post(f"{base_url}/users", json=payload, headers=headers)
    assert response.status_code == 201
    assert response.json()["name"] == "Arquam"