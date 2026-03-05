import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    """
    Базовый URL тестируемого API.
    """
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def session():
    """
    Создаёт HTTP-сессию requests.Session.
    """
    session = requests.Session()
    yield session
    session.close()
