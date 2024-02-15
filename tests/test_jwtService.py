import unittest
from datetime import datetime
from unittest.mock import patch
from jose import JWTError
from src.schemas.tokenSchema import TokenData
from src.services.jwtService import jwtActuator


class TestJwtActuator(unittest.TestCase):
    def setUp(self):
        self.jwt_actuator = jwtActuator()

    def test_create_access_token(self):
        data = {"username": "test_user", "role": "admin"}
        mock_utcnow = datetime(2024, 2, 14, 12, 0, 0)
        with patch("datetime.datetime") as mock_datetime:
            mock_datetime.utcnow.return_value = mock_utcnow
            token = self.jwt_actuator.create_access_token(data)
            self.assertIsNotNone(token)

    def test_verify_token_valid(self):
        token = "valid_token"
        data = {"username": "test_user", "role": "admin"}
        expected_token_data = TokenData(username="test_user", role="admin")
        with patch("jose.jwt.decode") as mock_decode:
            mock_decode.return_value = data
            token_data = self.jwt_actuator.verify_token(token, JWTError)
            self.assertEqual(token_data, expected_token_data)

    def test_verify_token_invalid(self):
        token = "invalid_token"
        with patch("jose.jwt.decode", side_effect=JWTError):
            with self.assertRaises(JWTError):
                self.jwt_actuator.verify_token(token, JWTError)
