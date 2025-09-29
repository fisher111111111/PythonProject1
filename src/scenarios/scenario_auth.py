import requests
from src.api.auth_client import AuthApiClient

class AuthScenario:
    def __init__(self, auth_client:AuthApiClient):
        self.auth_client = auth_client

    def right_create_auth(self):
        ''' Сценарий 1: авторизация и получение токена с валидными данными '''
        create_auth = self.auth_client.create_auth_client()
        if  create_auth.status_code != 201:  # это для сценария
            create_auth.raise_for_status()
        # print('Получен ожидаемый статус код:', create_auth.status_code, create_auth.text)
        return create_auth

# if __name__ == "__main__":
#     auth_check = AuthApiClient(requests)
#     hc = AuthScenario(auth_check)
#     hc.right_create_auth()

    def wrong_create_auth(self):
        '''Сценарий 2: попытка авторизации с невалидными данными '''
        non_create_auth = self.auth_client.non_auth_client()
        if non_create_auth.status_code != 200:
            non_create_auth.raise_for_status()
        # print ("Получен ожидаемый статус код", non_create_auth.status_code, non_create_auth.text)
        return  non_create_auth

# if __name__ == "__main__":
#     auth_check = AuthApiClient(requests)
#     hc = AuthScenario(auth_check)
#     hc.wrong_create_auth()