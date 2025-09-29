import requests
from datetime import timedelta
from pydantic import BaseModel, Field
from typing import Optional
import random
from faker import Faker
import os
from dotenv import load_dotenv
from enums.constant_of_url import ConstURL

load_dotenv()
fake = Faker()
BASE_URL = ConstURL.BASE_URL.value

class BookingCheckDates(BaseModel):
    checkin: str
    checkout: str

class BookingResponseData(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingCheckDates
    additionalneeds: Optional[str] = None


""" Класс для генерации проверок кода директории src """

BASE_URL = ConstURL.BASE_URL.value

class BookingAuthData:
    def make_auth_data(self):
        """Создаем и возвращаем данные для авторизации """
        auth_data = os.getenv("VALID_USERNAME"), os.getenv("VALID_PASSWORD")
        return auth_data

# if __name__ == "__main__":  # Проверка содержания отправляемого тела запроса
#     auth = BookingAuthData()
#     auth_data = auth.make_auth_data()
#     print(auth_data)

    def non_auth_data(self):
        """ Неправильные данные для авторизации"""
        wrong_auth_data = {
            "username": os.getenv("INVALID_USERNAME"),
            "password": os.getenv("INVALID_PASSWORD")
        }
        return wrong_auth_data

    def auth_token(self):
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
        token_session.auth = (os.getenv("VALID_USERNAME"), os.getenv("VALID_PASSWORD"))
        booking_token = response.json()['token']
        token_session.headers.update({"Cookie": f'token={booking_token}'})
        return token_session


class GenerateDates:
    def generate_booking_dates(self):
        """Генерация случайных дат checkin и checkout"""
        start_date = fake.date_between(start_date="today", end_date="+1m")
        end_date = start_date + timedelta(days=random.randint(1, 10))
        return {
            'checkin': start_date.strftime('%Y-%m-%d'),
            'checkout': end_date.strftime('%Y-%m-%d')
        }

    def booking_data(self):
        """Создание данных букинга"""
        self.dates = self.generate_booking_dates()
        return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": self.dates,
        "additionalneeds": "Breakfast"
    }
#
# # if __name__ == "__main__":  # Проверка содержания отправляемого тела запроса
# #     req = GenerateDates()
# #     request_data = req.booking_data()
# #     print(request_data)

    def wrong_booking_data(self):
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

    def upd_booking_data(self):
        """Данные для полного изменения букинга"""
        self.dates = self.generate_booking_dates()
        return {
            "firstname": "Updater",
            "lastname": "Updatenberg",
            "totalprice": fake.random_int(min=100, max=10000),
            "depositpaid": False,
            "bookingdates": self.dates,
            "additionalneeds": "Dinner"
        }

    def patch_booking_data(self):
        """Данные для частичного изменения букинга"""
        return {
            "firstname": "Patcheson",
            "lastname": "Patchey"
        }
