import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root_redirect():
    # Arrange: Test client is set up above
    # Act: Make a GET request to the root URL
    response = client.get("/")
    # Assert: Should redirect (307 or 302)
    assert response.status_code in (307, 302)

def test_get_activities():
    # Arrange: Test client is set up above
    # Act: Make a GET request to /activities
    response = client.get("/activities")
    # Assert: Should return 200 and a JSON dict
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
