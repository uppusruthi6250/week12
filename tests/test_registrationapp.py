
from app import app


def test_home_page():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200


def test_registration_success():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.post(
            "/submit",
            data={
                "username": "Sruthi",
                "password": "abc123"
            }
        )

        assert response.status_code == 200
        assert b"Registration successful" in response.data


def test_short_password():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.post(
            "/submit",
            data={
                "username": "Sruthi",
                "password": "123"
            }
        )

        assert response.status_code == 400
