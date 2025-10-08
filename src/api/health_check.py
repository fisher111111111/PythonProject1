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

    def broke_health_check(self):
        response = self.health_check.post(f"{self.base_url}{self.ping}")
        return response
