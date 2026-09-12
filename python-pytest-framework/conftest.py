import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"  # API change

@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json"
    }