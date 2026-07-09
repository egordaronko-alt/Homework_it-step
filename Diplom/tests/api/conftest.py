import pytest
import requests


@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    })
    yield session
    session.close()
