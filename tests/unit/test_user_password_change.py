from app.models.user import User


def test_change_password_updates_hash():
    user = User(
        first_name="Test",
        last_name="User",
        email="test@example.com",
        username="testuser",
        password=User.hash_password("OldPass123!")
    )

    old_hash = user.password
    user.change_password("OldPass123!", "NewPass123!")

    assert user.verify_password("NewPass123!")
    assert user.password != old_hash