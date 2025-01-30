import pytest  # type: ignore
from fastapi.testclient import TestClient  # type: ignore

from fast_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)
