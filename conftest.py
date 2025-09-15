import pytest
import requests
from faker import Faker
from src.enums.constant_of_url import ConstURL
import time
from src.scenarios.scenario_ping import PingScenario
from src.enums.constant_of_headers import ConstHeaders
from dotenv import load_dotenv
import os

load_dotenv()
fake = Faker()
BASE_URL = ConstURL.BASE_URL.value

from scenarios.scenario_ping import PingScenario
from src.api.health_check import HealthCheck


@pytest.fixture(scope="module")
def ping_check():
    """Фикстура создает экземпляр PingScenario с правильными зависимостями"""
    session = requests.Session()
    health_check = HealthCheck(session)
    return PingScenario(health_check)

# Фикстура получения времени ответа сервера
@pytest.fixture(scope="module")
def time_ping():
    start_time = time.perf_counter()
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000  # Преобразование результата в миллисекунды
    return execution_time

# Фикстура генерации отправляемых данных
@pytest.fixture(scope="session")
def booking_data():
    """Создание данных букинга"""
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

# Фикстура генерации отправляемых данных
@pytest.fixture(scope="session")
def wrong_booking_data():
    """Неправильные данные букинга"""
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
    """Данные для полного изменения букинга"""
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

# Фикстура для частично изменённых отправляемых данных
@pytest.fixture(scope="session")
def patch_booking_data():
    """Данные для частичного изменения букинга"""
    return {
        "firstname": "Patcheson",
        "lastname": "Patchey"
        }


# Фикстура для получения bookingid
@pytest.fixture(scope="session")
def booking_id(booking_data):
    """Получение тела ответа на POST запрос """
    response = requests.post(f"{BASE_URL}/booking", json=booking_data)
    assert response.status_code == 200
    bookingid = response.json()["bookingid"]
    # print(bookingid)
    # print(response.json())
    return bookingid

# bookingid = booking_id(booking_data())
# print(bookingid)

# Фикстураа авторизации
@pytest.fixture(scope="session")
def make_auth_data():
    """Правильные данные для авторизации"""
    auth_data = {
        "username": os.getenv("VALID_USERNAME"),
        "password": os.getenv("VALID_PASSWORD")
    }
    return auth_data

# Фикстураа ошибочной авторизации
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
    """Создание сессии с авторизацией и возврат объекта сессии"""
    token_session = requests.Session()
    auth_data = {
        "username": os.getenv("VALID_USERNAME"),
        "password": os.getenv("VALID_PASSWORD")
    }
    response = token_session.post(f"{BASE_URL}/auth", json=auth_data)
    if response.status_code not in (200, 201):
        response.raise_for_status()
    booking_auth = token_session.auth = (os.getenv("VALID_USERNAME"), os.getenv("VALID_PASSWORD") )
    booking_token = response.json()['token']
    token_session.headers.update({"Cookie": f'token={booking_token}'})
    # print(token_session.headers)
    # print(booking_auth)
    return token_session

@pytest.fixture(scope="module")
def test_ping():
    return PingScenario(ConstURL.BASE_URL)

# Фикстура создания сессии авторизации и возврат объекта сессии
#  @pytest.fixture(scope="session")
# def auth_session():
#     """Создание сессии с авторизацией и возврат объекта сессии"""
#     session = requests.Session()
#     session.headers.update(ConstHeaders)
#     auth_response = session.post(f'{BASE_URL}/auth', json={"username": "admin", "password": "password123"})
#     token = auth_response.json().get("token")
#     assert token is not None, "Токен в ответе отсутствует"
#     session.headers.update({"Cookie": f"token={token}"})
#     return session

# # Фикстура для получения и удаления bookingid
# # @pytest.fixture(scope="session")
# def create_del_booking_id(booking_data, auth_token):
#     response1 = requests.post(f"{BASE_URL}/booking", json=booking_data)
#     assert response1.status_code == 200
#     booking_id = response1.json()["bookingid"]
#     print(booking_id)
#     # yield booking_id
#
# # Фикстура для удаления bookingid
# # @pytest.fixture(scope="session")
# def del_booking_id(booking_id):
#     response2 = auth_token.delete(f"{BASE_URL}/booking/{booking_id}")
#     assert response2.status_code in (200, 201)
#     delete_id = response2.status_code
#     print(response2.status_code)
#     return delete_id
#
# create_del_booking_id(booking_data(), auth_token)
# del_booking_id(booking_id)







