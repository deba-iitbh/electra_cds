from src.constants import pwd_context
from src.services.hashService import Hash
from unittest import TestCase
from unittest.mock import patch


class TestHashService(TestCase):
    def setUp(self):
        self.hash_service = Hash()

    def test_verify_password_correct(self):
        plain_password = "password123"
        hashed_password = pwd_context.hash(plain_password)
        self.assertTrue(
            self.hash_service.verify_password(plain_password, hashed_password)
        )

    def test_verify_password_incorrect(self):
        plain_password = "password123"
        incorrect_password = "wrongpassword"
        hashed_password = pwd_context.hash(plain_password)
        self.assertFalse(
            self.hash_service.verify_password(incorrect_password, hashed_password)
        )

    def test_get_password_hash(self):
        password = "password123"
        expected_hash = pwd_context.hash(password)
        with patch.object(pwd_context, "hash") as mock_hash:
            mock_hash.return_value = expected_hash
            result = self.hash_service.get_password_hash(password)
            self.assertEqual(result, expected_hash)
