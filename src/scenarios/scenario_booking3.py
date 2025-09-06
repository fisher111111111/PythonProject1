from src.enums.constant_of_url import ConstURL
import requests
from src.api.health_check import HealthCheck

class HealthCheckScenario:
    def __init__(self, health_client: HealthCheck):
        self.health_client = health_client
        self.base_url = ConstURL.BASE_URL.value

    def broke_health_check(self):
        response = self.health_client.post(f'{self.base_url}/ping')
        if response.status_code == 201:
            print("Что-то пошло не так и Ping прошел")
        else:
            print("Запрос ожидаемо не прошел")
        return response.status_code
# if __name__ == "__main__":
#     health_client = requests.Session()
#     hc1 = HealthCheckScenario(health_client)
#     result = hc1.broke_health_check()
#     print(result)