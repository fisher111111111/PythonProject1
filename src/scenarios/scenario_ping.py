import requests
from src.api.health_check import HealthCheck

import time
from datetime import timedelta

class PingScenario:
    def __init__(self, ping_check: HealthCheck):
        self.ping_check = ping_check

    def right_ping (self):
        '''Сценарий 1: проверяем ping верным методом'''
        ping = self.ping_check.make_health_check()
        if ping.status_code != 201:  # это для сценария
            ping.raise_for_status()
        print('Получен ожидаемый статус код:', ping.status_code)
        return ping

# if __name__ == "__main__":
#     health_check = HealthCheck(requests)
#     hc = PingScenario(health_check)
#     hc.right_ping()

    def wrong_ping (self):
        '''Сценарий 2: проверяем ping неверным методом '''
        ping = self.ping_check.broke_health_check()
        if ping.status_code == 201:   # это для сценария
            print("Что-то пошло не так и Ping прошел")
        else:
            print(f" Получен ожидаемый статус-код: {ping.status_code}")
        return ping

# if __name__ == "__main__":
#     health_check = HealthCheck(requests)
#     hc = PingScenario(health_check)
#     hc.wrong_ping()


