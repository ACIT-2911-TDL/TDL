from unittest import TestCase
import requests


class TestUser(TestCase):
    def setUp(self) -> None:
        self.create_user_data = {"username": "ArchXII", "password": "P@ssw0rd"}

    def test_add_valid_user(self):
        r = requests.post("http://localhost:5000/CreateUser", json=self.create_user_data)
        self.assertEqual(r.status_code, 204)
