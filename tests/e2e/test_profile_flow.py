import requests
from uuid import uuid4
import pytest


@pytest.mark.e2e
def test_password_change_flow(page, fastapi_server):
    base_url = fastapi_server.rstrip("/")
    password = "OldPass123!"
    user = {
        "first_name": "E2E",
        "last_name": "User",
        "email": f"e2e{uuid4()}@example.com",
        "username": f"e2e_{uuid4().hex[:8]}",
        "password": password,
        "confirm_password": password,
    }
    reg = requests.post(f"{base_url}/auth/register", json=user)
    assert reg.status_code == 201

    page.goto(f"{base_url}/login")
    page.fill("#username", user["username"])
    page.fill("#password", password)
    page.click("button[type=submit]")
    page.wait_for_url(f"{base_url}/dashboard")

    page.goto(f"{base_url}/profile")
    page.fill("#currentPassword", password)
    page.fill("#newPassword", "NewPass123!")
    page.fill("#confirmNewPassword", "NewPass123!")
    page.click("#passwordForm button[type=submit]")
    page.wait_for_timeout(500)

    page.once("dialog", lambda dialog: dialog.accept())
    page.click("#layoutLogoutBtn")
    page.wait_for_url(f"{base_url}/login")

    page.fill("#username", user["username"])
    page.fill("#password", "NewPass123!")
    page.click("button[type=submit]")
    page.wait_for_url(f"{base_url}/dashboard")