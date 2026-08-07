import requests
import pytest

BASE_URL = "https://reqres.in/api"

@pytest.fixture
def base_url():
    return BASE_URL