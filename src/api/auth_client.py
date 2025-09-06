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
        return response.json()['token'], auth_data

auth_token = requests.Session()
hc1 = AuthApiClient(auth_token)
token, auth_data = hc1.create_auth_client()
print(token, auth_data)
#
# result1 = hc1.create_auth_client()
# print (result1)

#     def non_create_auth_client(self):
#         '''
#         Отправляет запрос на создание токена аутентификации.
#         '''
#         non_auth_data = {
#             "username": os.getenv("INVALID_USERNAME"),
#             "password": os.getenv("INVALID_PASSWORD")
#         }
#         response = self.auth_token.post(f"{self.base_url}/auth", json=non_auth_data)
#         if response.status_code not in (200, 201):
#             response.raise_for_status()
#         print(response.status_code)
#         return response.json()['reason']
#
# # auth_token = requests.Session()
# # hc2 = AuthApiClient(auth_token)
# # result2 = hc2.non_create_auth_client()
# # print(result2)
