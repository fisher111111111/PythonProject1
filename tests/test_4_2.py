import requests
from constant import BASE_URL
from constant import VALID_CREDENTIALS
from constant import INVALID_CREDENTIALS

# Тесты для Auth - CreateToken
def test_auth_create_token():
    response = requests.post(f"{BASE_URL}/auth", json=VALID_CREDENTIALS)
    assert response.status_code == 200
    assert "token" in response.json()
    assert isinstance(response.json()["token"], str)


def test_auth_invalid_credentials():
    response = requests.post(f"{BASE_URL}/auth", json=INVALID_CREDENTIALS)
    assert  "token" not in response.json()


def test_auth_missing_fields():
    response = requests.post(f"{BASE_URL}/auth", json={})
    assert  "token" not in response.json()


def test_auth_empty_fields():
    response = requests.post(f"{BASE_URL}/auth", json={"username": "", "password": ""})
    assert  "token" not in response.json()


def test_auth_invalid_content_type():
    headers = {"Content-Type": "text/plain"}
    response = requests.post(f"{BASE_URL}/auth", json=VALID_CREDENTIALS, headers=headers)
    assert "token" not in response.json()


def test_auth_invalid_json():
    response = requests.post(f"{BASE_URL}/auth", data="invalid json", headers={"Content-Type": "application/json"})
    assert response.status_code == 400


# Тесты для Booking - GetBookingIds
def test_get_booking_ids():
    response = requests.get(f"{BASE_URL}/booking")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all("bookingid" in item for item in response.json())


def test_get_booking_ids_filter_firstname():
    response = requests.get(f"{BASE_URL}/booking?firstname=Sally")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all("bookingid" in item for item in response.json())


def test_get_booking_ids_filter_lastname():
    response = requests.get(f"{BASE_URL}/booking?lastname=Brown")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all("bookingid" in item for item in response.json())


def test_get_booking_ids_filter_checkin():
    response = requests.get(f"{BASE_URL}/booking?checkin=2015-01-01")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all("bookingid" in item for item in response.json())


def test_get_booking_ids_filter_checkout():
    response = requests.get(f"{BASE_URL}/booking?checkout=2015-01-01")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all("bookingid" in item for item in response.json())


def test_get_booking_ids_combined_filter():
    response = requests.get(f"{BASE_URL}/booking?firstname=Sally&lastname=Brown&checkin=2015-01-01&checkout=2015-01-01")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all("bookingid" in item for item in response.json())


def test_get_booking_ids_invalid_date_format():
    response = requests.get(f"{BASE_URL}/booking?checkin=23-02-2013")
    assert not (200 <= response.status_code < 300)


# Тесты для Booking - GetBooking
def test_get_booking_valid_id(booking_id):
    response = requests.get(f"{BASE_URL}/booking/{booking_id}")
    assert response.status_code == 200
    assert "firstname" in response.json()
    assert "lastname" in response.json()
    assert "totalprice" in response.json()
    assert "depositpaid" in response.json()
    assert "bookingdates" in response.json()


def test_get_booking_invalid_id():
    response = requests.get(f"{BASE_URL}/booking/999999")
    assert response.status_code == 404


def test_get_booking_invalid_id_format():
    response = requests.get(f"{BASE_URL}/booking/abc")
    assert not (200 <= response.status_code < 300)


# Тесты для Booking - CreateBooking
def test_create_booking_valid_data():
    booking_data = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-02"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(f"{BASE_URL}/booking", json=booking_data)
    assert response.status_code == 200
    assert "bookingid" in response.json()


def test_create_booking_missing_fields():
    booking_data = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True
        }
    response = requests.post(f"{BASE_URL}/booking", json=booking_data)
    assert not (200 <= response.status_code < 300)

# Тесты для UpdateBooking
def test_update_booking_valid_data(auth_token, booking_id):
    booking_data = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-02"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {"Cookie": f"token={auth_token}"}
    response = requests.put(f"{BASE_URL}/booking/{booking_id}", json=booking_data, headers=headers)
    assert response.status_code == 200
    assert "firstname" in response.json()
    assert "lastname" in response.json()
    assert "totalprice" in response.json()
    assert "depositpaid" in response.json()
    assert "bookingdates" in response.json()
    assert "additionalneeds" in response.json()


def test_update_booking_invalid_id(auth_token):
    booking_data = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-02"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {"Cookie": f"token={auth_token}"}
    response = requests.put(f"{BASE_URL}/booking/999999", json=booking_data, headers=headers)
    assert response.status_code == 405


def test_update_booking_invalid_token():
    booking_data = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-02"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {"Cookie": "token=invalid_token"}
    response = requests.put(f"{BASE_URL}/booking/booking_id", json=booking_data, headers=headers)
    assert response.status_code == 403

def test_update_booking_without_authorization(booking_id):
    booking_data = {
    "firstname": "John",
    "lastname": "Doe",
    "totalprice": 100,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2023-01-01",
        "checkout": "2023-01-02"
    },
    "additionalneeds": "Breakfast"
    }
    response = requests.put(f"{BASE_URL}/booking/{booking_id}", json=booking_data)
    assert not (200 <= response.status_code < 300)


def test_update_booking_missing_fields(auth_token, booking_id):
    booking_data = {
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-02"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {"Cookie": f"token={auth_token}"}
    response = requests.put(f"{BASE_URL}/booking/{booking_id}", json=booking_data, headers=headers)
    assert not (200 <= response.status_code < 300)


# Тесты для Booking - PartialUpdateBooking
def test_partial_update_booking_valid_data(auth_token, booking_id):
    booking_data = {
        "firstname": "John",
        "lastname": "Doe"
    }
    headers = {"Cookie": f"token={auth_token}"}
    response = requests.patch(f"{BASE_URL}/booking/{booking_id}", json=booking_data, headers=headers)
    assert response.status_code == 200
    assert "firstname" in response.json()
    assert "lastname" in response.json()


def test_partial_update_booking_multiple_fields(auth_token, booking_id):
    booking_data = {
        "firstname": "John",
        "totalprice": 100
    }
    headers = {"Cookie": f"token={auth_token}"}
    response = requests.patch(f"{BASE_URL}/booking/{booking_id}", json=booking_data, headers=headers)
    assert response.status_code == 200
    assert "firstname" in response.json()
    assert "totalprice" in response.json()


def test_partial_update_booking_invalid_id(auth_token, booking_id):
    booking_data = {
        "firstname": "John",
        "lastname": "Doe"
    }
    headers = {"Cookie": f"token={auth_token}"}
    response = requests.patch(f"{BASE_URL}/booking/999999", json=booking_data, headers=headers)
    assert response.status_code == 405


def test_partial_update_booking_invalid_token(booking_id):
    booking_data = {
        "firstname": "John",
        "lastname": "Doe"
    }
    headers = {"Cookie": "token=invalid_token"}
    response = requests.patch(f"{BASE_URL}/booking/{booking_id}", json=booking_data, headers=headers)
    assert response.status_code == 403


def test_partial_update_booking_without_authorization(booking_id):
    booking_data = {
        "firstname": "John"
    }
    response = requests.patch(f"{BASE_URL}/booking/{booking_id}", json=booking_data)
    assert not (200 <= response.status_code < 300)


def test_partial_update_booking_empty_body(booking_id):
    booking_data = {}
    response = requests.patch(f"{BASE_URL}/booking/{booking_id}", json=booking_data)
    assert not (200 <= response.status_code < 300)


# Тесты для Booking - DeleteBooking
def test_delete_booking_valid_id(auth_token, booking_id):
    headers = {"Cookie": f"token={auth_token}"}
    response = requests.delete(f"{BASE_URL}/booking/{booking_id}", headers=headers)
    assert response.status_code == 201
    # Проверка, что бронирование удалено
    response = requests.get(f"{BASE_URL}/booking/{booking_id}")
    assert response.status_code == 404


def test_delete_booking_without_authorization(booking_id):
    response = requests.delete(f"{BASE_URL}/booking/{booking_id}")
    assert not (200 <= response.status_code < 300)


def test_delete_booking_invalid_id(auth_token):
    headers = {"Cookie": f"token={auth_token}"}
    response = requests.delete(f"{BASE_URL}/booking/999999", headers=headers)
    assert response.status_code == 405


def test_delete_booking_invalid_token(booking_id):
    headers = {"Cookie": "token=invalid_token"}
    response = requests.delete(f"{BASE_URL}/booking/{booking_id}", headers=headers)
    assert response.status_code == 403


# Тесты для Ping - HealthCheck
def test_ping_healthcheck():
    response = requests.get(f"{BASE_URL}/ping")
    assert response.status_code == 201
    assert response.text == "Created"


def test_ping_invalid_method1():
    response = requests.post(f"{BASE_URL}/ping")
    assert response.status_code == 404


def test_ping_invalid_method2():
    response = requests.put(f"{BASE_URL}/ping")
    assert response.status_code == 404


def test_ping_invalid_method3():
    response = requests.patch(f"{BASE_URL}/ping")
    assert response.status_code == 404


def test_ping_invalid_method4():
    response = requests.delete(f"{BASE_URL}/ping")
    assert response.status_code == 404