import pytest
import requests
from faker import Faker
from scenarios.scenario_auth import AuthScenario
from src.api.auth_client import AuthApiClient
from src.enums.constant_of_url import ConstURL
import time
from src.scenarios.scenario_ping import PingScenario
from src.api.health_check import HealthCheck
from dotenv import load_dotenv
import os

load_dotenv()
fake = Faker()
BASE_URL = ConstURL.BASE_URL.value

@pytest.fixture(scope="module")
def auth_check():
    """ для тестирования раздела Ping
    Фикстура создает экземпляр PingScenario с правильными зависимостями"""
    session = requests.Session()
    health_check = HealthCheck(session)
    return PingScenario(health_check)

@pytest.fixture(scope="module")
def auth_check_1():
    """ Для тестирования раздела Auth
    Фикстура создает экземпляр AuthScenario с правильными зависимостями"""
    session = requests.Session()
    auth = AuthApiClient(session)
    return AuthScenario(auth)

@pytest.fixture(scope="module")
def time_ping():
    """ для тестирования раздела Ping
        Фикстура для проверки времени ответа сервера"""
    start_time = time.perf_counter()
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000  # Преобразование результата в миллисекунды
    return execution_time

@pytest.fixture(scope="session")
def booking_data():
    """ Тестирование раздела Booking
    # Фикстура генерации отправляемых данных букинга """
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": "Breakfast"
    }

@pytest.fixture(scope="session")
def wrong_booking_data():
    """ Тестирование раздела Booking
    Фикстура генерации отправляемых Неправильных данных букинга"""
    return {
        "firstname": None,
        "lastname": None,
        "totalprice": fake.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": "Breakfast"
    }

# Фикстура для изменённых отправляемых данных
@pytest.fixture(scope="session")
def upd_booking_data():
    """Тестирование раздела Booking
    Данные для полного изменения букинга"""
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=10000),
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-05-06",
            "checkout": "2025-05-09"
        },
        "additionalneeds": "Dinner"
    }

@pytest.fixture(scope="session")
def patch_booking_data():
    """ Тестирование раздела Booking
    Данные для частичного изменения букинга"""
    return {
        "namew": "Patcheson",
        "name": "Patchey"
        }

@pytest.fixture(scope="session")
def make_auth_data():
    """Правильные данные для авторизации"""
    auth_data = os.getenv("VALID_USERNAME"), os.getenv("VALID_PASSWORD")

    return auth_data

@pytest.fixture(scope="session")
def non_auth_data():
    """ Неправильные данные для авторизации"""
    wrong_auth_data = {
        "username": os.getenv("INVALID_USERNAME"),
        "password": os.getenv("INVALID_PASSWORD")
    }
    return wrong_auth_data

@pytest.fixture(scope="session")
def auth_token():
    """ Тестирование раздела Booking
    Создание сессии с авторизацией"""
    token_session = requests.Session()
    auth_data = {
        "username": os.getenv("VALID_USERNAME"),
        "password": os.getenv("VALID_PASSWORD")
    }
    response = token_session.post(f"{BASE_URL}/auth", json=auth_data)
    if response.status_code not in (200, 201):
        response.raise_for_status()
    token_session.auth = (os.getenv("VALID_USERNAME"), os.getenv("VALID_PASSWORD") )
    booking_token = response.json()['token']
    token_session.headers.update({"Cookie": f'token={booking_token}'})
    return token_session

@pytest.fixture(scope="session")
def bookingids (get_booking_id):
    """ Тестирование раздела Booking
    Фикстура получения bookingid для общего списка букингов"""
    return [{ "bookingid": get_booking_id}]


""" Фикстуры для второго варианта тестов"""

@pytest.fixture(scope="session")
def get_booking_id(booking_data):
    """Тестирование раздела Booking - для второго варианта тестов
    Получение ID букинга """
    response = requests.post(f"{BASE_URL}/booking", json=booking_data)
    assert response.status_code == 200
    booking_id = response.json()["bookingid"]
    return booking_id

@pytest.fixture(scope="session")
def del_booking_id(get_booking_id, make_auth_data):
    """Тестирование раздела Booking - для второго варианта тестов
    Фикстура для удаления по ID букинга """
    yield get_booking_id
    response = requests.delete(f"{BASE_URL}/booking/{get_booking_id}", auth=make_auth_data)
    assert response.status_code == 201
    return response.text
