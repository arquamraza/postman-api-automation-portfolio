import requests

def test_user_api():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)
    
    assert response.status_code == 200
    assert response.json()['name'] == "Leanne Graham"