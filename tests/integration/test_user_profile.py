import requests
from uuid import uuid4


def _register_and_login(base_url: str, password: str):
    user_data = {
        "first_name": "Test",
        "last_name": "User",
        "email": f"test{uuid4()}@example.com",
        "username": f"testuser_{uuid4().hex[:8]}",
        "password": password,
        "confirm_password": password,
    }
    reg = requests.post(f"{base_url}/auth/register", json=user_data)
    assert reg.status_code == 201
    login = requests.post(f"{base_url}/auth/login", json={"username": user_data["username"], "password": password})
    assert login.status_code == 200
    token = login.json()["access_token"]
    return user_data, token


def test_update_profile(fastapi_server):
    base_url = fastapi_server.rstrip("/")
    user_data, token = _register_and_login(base_url, "SecurePass123!")

    new_email = f"new{uuid4()}@example.com"
    resp = requests.put(
        f"{base_url}/users/me",
        json={"email": new_email},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 200
    assert resp.json()["email"] == new_email

    get_resp = requests.get(
        f"{base_url}/users/me", headers={"Authorization": f"Bearer {token}"}
    )
    assert get_resp.status_code == 200
    assert get_resp.json()["email"] == new_email


def test_change_password(fastapi_server):
    base_url = fastapi_server.rstrip("/")
    user_data, token = _register_and_login(base_url, "OldPass123!")

    change_resp = requests.put(
        f"{base_url}/users/me/password",
        json={
            "current_password": "OldPass123!",
            "new_password": "NewPass123!",
            "confirm_new_password": "NewPass123!",
        },
        headers={"Authorization": f"Bearer {token}"},
    )
    assert change_resp.status_code == 200

    # Old password should fail
    old_login = requests.post(
        f"{base_url}/auth/login",
        json={"username": user_data["username"], "password": "OldPass123!"},
    )
    assert old_login.status_code == 401

    # New password should work
    new_login = requests.post(
        f"{base_url}/auth/login",
        json={"username": user_data["username"], "password": "NewPass123!"},
    )
    assert new_login.status_code == 200