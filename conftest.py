import pytest
import requests
from faker import Faker
from src.enums.constant_of_url import ConstURL
from src.enums.constant_of_headers import ConstHeaders

fake = Faker()
BASE_URL = ConstURL.BASE_URL.value

@pytest.fixture(scope="session")
def auth_token():
    response = requests.post(f'{BASE_URL}/auth', json=ConstHeaders)
    assert response.status_code == 200, "Ошибочный статус-код"
    return response.json()["token"]

@pytest.fixture(scope="session")
def booking_data():
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

# Фикстура для создания бронирования и возврата bookingid
@pytest.fixture(scope="session")
def booking_id(booking_data):
    response = requests.post(f"{BASE_URL}/booking", json=booking_data)
    assert response.status_code == 200
    return response.json()["bookingid"]

# Фикстура создания сессии авторизации и возврат объекта сессии
@pytest.fixture(scope="session")
def auth_session():
    """Create session with authorization and return object of session"""
    session = requests.Session()
    session.headers.update(ConstHeaders)

    auth_response = session.post(f'{BASE_URL}/auth', json={"username": "admin", "password": "password123"})
    token = auth_response.json().get("token")
    assert token is not None, "Токен в ответе отсутствует"

    session.headers.update({"Cookie": f"token={token}"})
    return session