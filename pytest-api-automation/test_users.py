def test_get_users(base_url):
    response = requests.get(f"{base_url}/users?page=2")
    assert response.status_code == 200
    assert "data" in response.json()

def test_create_user(base_url):
    data = {"name": "Arquam", "job": "SDET"}
    response = requests.post(f"{base_url}/users", json=data)
    assert response.status_code == 201

def test_update_user(base_url):
    data = {"name": "Arquam Updated"}
    response = requests.put(f"{base_url}/users/2", json=data)
    assert response.status_code == 200