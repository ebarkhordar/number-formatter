from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_format_number_int_3_digits():
    response = client.post(
        "/numbers/",
        json={"input": 500},
    )
    assert response.status_code == 200
    assert response.json() == {
        "formatted": "500",
    }


def test_format_number_int_4_digits():
    response = client.post(
        "/numbers/",
        json={"input": 3400},
    )
    assert response.status_code == 200
    assert response.json() == {
        "formatted": "3.5k",
    }


def test_format_number_int_millions():
    response = client.post(
        "/numbers/",
        json={"input": 1000000},
    )
    assert response.status_code == 200
    assert response.json() == {
        "formatted": "1M",
    }


def test_format_number_float_millions():
    response = client.post(
        "/numbers/",
        json={"input": 2500000.34},
    )
    assert response.status_code == 200
    assert response.json() == {
        "formatted": "2.5M",
    }


def test_format_number_int_billions():
    response = client.post(
        "/numbers/",
        json={"input": 1123456789},
    )
    assert response.status_code == 200
    assert response.json() == {
        "formatted": "1.1B",
    }
