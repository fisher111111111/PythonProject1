from src.enums.constant_of_url import ConstURL
import requests

class HealthCheck:
    def __init__(self, health_check):
        self.health_check = health_check
        self.base_url = ConstURL.BASE_URL.value
        self.ping = ConstURL.PING_ENDPOINT.value

    def make_health_check(self):
        response = self.health_check.get(f"{self.base_url}{self.ping}")
        # if response.status_code != 201:  # это для сценария
        #     response.raise_for_status()
        return response

# if __name__ == "__main__":
#     health_check = requests.Session()
#     hc = HealthCheck(health_check)
#     result = hc.make_health_check()
#     print(result)

    def broke_health_check(self):
        response = self.health_check.post(f"{self.base_url}{self.ping}")
        # if response.status_code == 201:   # это для сценария
        #     print("Что-то пошло не так и Ping прошел")
        # else:
        #     print("Запрос ожидаемо не прошел")
        return response

# if __name__ == "__main__":
#     health_check = requests.Session()
#     hc1 = HealthCheck(health_check)
#     result = hc1.broke_health_check()
#     print(result)