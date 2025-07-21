from src.enums.constant_of_url import ConstURL
import requests
from dotenv import load_dotenv
import os

load_dotenv()


class AuthApiClient:
    def __init__(self, auth_token):
        self.auth_token = auth_token
        self.base_url = ConstURL.BASE_URL.value

    def create_auth_client(self):
        """Отправляет запрос на создание токена аутентификации."""
        auth_data = {
            "username": os.getenv("VALID_USERNAME"),
            "password": os.getenv("VALID_PASSWORD")
        }
        response = self.auth_token.post(f"{self.base_url}/auth", json=auth_data)
        if response.status_code not in (200, 201):
            response.raise_for_status()
        print(response.status_code)
        return response.json()['token']

    def non_create_auth_client(self):
        """Отправляет запрос на создание токена аутентификации."""
        auth_data = {
            "username": os.getenv("INVALID_USERNAME"),
            "password": os.getenv("INVALID_PASSWORD")
        }
        response = self.auth_token.post(f"{self.base_url}/auth", json=auth_data)
        if response.status_code not in (200, 201):
            response.raise_for_status()
        print(response.status_code)
        return response.json()['reason']


auth_token = requests.Session()
hc = AuthApiClient(auth_token)
result1 = hc.create_auth_client()
print(result1)
hc = AuthApiClient(auth_token)
result2 = hc.non_create_auth_client()
print(result2)
