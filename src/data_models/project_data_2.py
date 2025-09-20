from datetime import timedelta
from pydantic import BaseModel, Field
from typing import Optional
import random
from faker import Faker
import os

fake = Faker()

class BookingAuthData:
    def make_auth_data(self):
        """Создаем и возвращаем данные для переиспользования """
        return {
            "username": os.getenv("VALID_USERNAME"),
            "password": os.getenv("VALID_PASSWORD")
        }

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

class BookingRequestCheckDates(BaseModel):
    checkin: str
    checkout: str

class BookingRequestData(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingRequestCheckDates
    additionalneeds: Optional[str] = None

    @staticmethod
    def generate_booking_dates():
        """Генерация случайных дат checkin и checkout"""
        start_date = fake.date_between(start_date="today", end_date="+1m")
        end_date = start_date + timedelta(days=random.randint(1, 10))
        return {
            'checkin': start_date.strftime('%Y-%m-%d'),
            'checkout': end_date.strftime('%Y-%m-%d')
        }

    @classmethod
    def booking_data(cls):
        """Создание данных букинга"""
        # first_name = fake.first_name()
        # last_name = fake.last_name()
        # total_price = fake.random_int(min=100, max=10000)
        # deposit_paid = True
        # additional_needs = "Breakfast"
        # generated_dates = cls.generate_booking_dates()
        # booking_request_check_dates = BookingRequestCheckDates(**generated_dates)
        # # Создание экземпляра класса с правильными данными
        # instance = cls(firstname=first_name, lastname=last_name, totalprice=total_price, depositpaid=deposit_paid, bookingdates=booking_request_check_dates, additionalneeds=additional_needs)
        # # Возвращаем JSON представление данных
        # return                  instance.model_dump_json(indent=4)
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

if __name__ == "__main__":  # Проверочный пример
    request_data = BookingRequestData.booking_data()
    print(request_data)  # Выведем JSON-данные
