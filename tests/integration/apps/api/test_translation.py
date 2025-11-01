import pytest
from fastapi.testclient import TestClient

from apps.api.main import app


@pytest.fixture
def test_client() -> TestClient:
    client = TestClient(app)
    return client


@pytest.mark.integration
def test_hello_world(test_client: TestClient) -> None:
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


@pytest.mark.integration
def test_post_translation(test_client: TestClient) -> None:
    response = test_client.post(
        "/definitions",
        json=dict(
            word="circuitous",
            context=(
                "Taxi drivers now struggle to take people "
                "on circuitous but profitable routes, since "
                "apps such as Lyft and Uber tell them exactly"
                "where to go."
            ),
        ),
    )
    response_json = response.json()
    assert response.status_code == 200
    assert len(response_json["definitions"]) > 0
    assert len(response_json["definitions"][0]) > 0
