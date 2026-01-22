from PythonProject1.src.enums.constant_of_url import ConstURL
from dotenv import load_dotenv
import os

load_dotenv()

class AuthApiClient:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = ConstURL.BASE_URL.value
        self.auth = ConstURL.AUTH_ENDPOINT.value

    def create_auth_client(self):
        """Отправляет запрос на создание токена аутентификации."""
        auth_data = {
            "username": os.getenv("VALID_USERNAME"),
            "password": os.getenv("VALID_PASSWORD")
        }
        response = self.auth_session.post(f"{self.base_url}/{self.auth}", json=auth_data)
        return response

    def non_auth_client(self):
        """Отправляет запрос на создание токена аутентификации."""
        non_auth_data = {
            "username": os.getenv("INVALID_USERNAME"),
            "password": os.getenv("INVALID_PASSWORD")
        }
        response = self.auth_session.post(f"{self.base_url}/{self.auth}",json=non_auth_data)
        return response