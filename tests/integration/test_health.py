from fastapi.testclient import TestClient

from knowledge_agent.main import app


def test_health_checks_database() -> None:
    response = TestClient(app).get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "ok"}


def test_info_returns_application_metadata() -> None:
    response = TestClient(app).get("/info")

    assert response.status_code == 200
    assert response.json() == {
        "name": "Enterprise Knowledge Agent",
        "version": "0.1.0",
    }
