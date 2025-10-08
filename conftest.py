import pytest
import requests
from scenarios.scenario_auth import AuthScenario
from src.api.auth_client import AuthApiClient
from src.enums.constant_of_url import ConstURL
from src.data_models.project_data import BookingAuthData, BookingResponseData, BookingWrongData
from src.data_models.project_data_patch import BookingPatchData
import time
from src.scenarios.scenario_ping import PingScenario
from src.api.health_check import HealthCheck

BASE_URL = ConstURL.BASE_URL.value
BOOKING = ConstURL.BOOKING_ENDPOINT.value

@pytest.fixture(scope="session")
def ping_check():
    """ для тестирования раздела Ping
    Фикстура создает экземпляр PingScenario с правильными зависимостями"""
    session = requests.Session()
    health_check = HealthCheck(session)
    return PingScenario(health_check)

@pytest.fixture(scope="session")
def auth_check():
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
def fake_booking_data():
    """ Тестирование раздела Booking
    # Фикстура генерации отправляемых данных букинга """
    data_create = BookingResponseData.fake_booking_data()
    return data_create

# Фикстура для изменённых отправляемых данных
@pytest.fixture(scope="session")
def upd_booking_data():
    """Тестирование раздела Booking
    Данные для полного изменения букинга"""
    data_update = BookingResponseData.fake_upd_booking_data()
    return data_update

@pytest.fixture(scope="session")
def patch_booking_data():
    """ Тестирование раздела Booking
    Данные для частичного изменения букинга"""
    data_patch = BookingPatchData.fake_patch_booking_data()
    return data_patch

@pytest.fixture(scope="session")
def fake_wrong_booking_data():
    """ Тестирование раздела Booking
    Фикстура генерации отправляемых Неправильных данных букинга"""
    data_wrong_create = BookingWrongData.fake_wrong_booking_data()
    return data_wrong_create

@pytest.fixture(scope="session")
def make_auth_data():
    """Правильные данные для авторизации"""
    auth_data = BookingAuthData()
    return auth_data.make_auth_data()

@pytest.fixture(scope="session")
def non_auth_data():
    """ Неправильные данные для авторизации"""
    wrong_auth_data = BookingAuthData()
    return wrong_auth_data.non_auth_data()

@pytest.fixture(scope="session")
def auth_token():
    """ Тестирование раздела Booking
    Создание сессии с авторизацией"""
    data_token = BookingAuthData()
    return data_token.auth_token()

@pytest.fixture(scope="session")
def bookingids (get_booking_id):
    """ Тестирование раздела Booking
    Фикстура получения bookingid для общего списка букингов"""
    return [{ "bookingid": get_booking_id}]

""" Фикстуры для второго варианта тестов"""

@pytest.fixture(scope="session")
def get_booking_id(fake_booking_data):
    """Тестирование раздела Booking - для второго варианта тестов
    Получение ID букинга """
    response = requests.post(f"{BASE_URL}/booking", json=fake_booking_data)
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
