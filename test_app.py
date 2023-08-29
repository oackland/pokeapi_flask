#  Copyright (c) 2023 Oackland Toro
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

import unittest

from app import (
    create_app,
    db,
    User,
)  # Adjust the import based on your actual file structure


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    WTF_CSRF_ENABLED = False


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config.from_object(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_login(self):
        # Add a test user to the database
        user = User(username="test", email="test@test.com")
        user.set_password("password")
        db.session.add(user)
        db.session.commit()

        # Try to login
        response = self.client.post(
            "/login",
            data={"username": "test", "password": "password"},
            follow_redirects=True,
        )

        self.assertIn(
            b"Successfully logged in", response.data
        )  # Replace with the actual success message

    def test_unauthorized_access(self):
        # Try to access a protected page
        response = self.client.get("/protected", follow_redirects=True)
        self.assertIn(
            b"danger", response.data
        )  # Replace with the actual unauthorized access message


if __name__ == "__main__":
    unittest.main()
