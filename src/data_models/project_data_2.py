
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

class BookingResponseData (BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingCheckDates
    additionalneeds: Optional[str]=None

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

    def generate_booking_dates(self):
        """Генерация случайных дат checkin и checkout"""
        start_date = fake.date_between(start_date="today", end_date="+1m")
        end_date = start_date + timedelta(days=random.randint(1,10))
        return {
            'checkin': start_date.strftime('%Y-%m-%d'),
            'checkout': end_date.strftime('%Y-%m-%d')
        }

    def booking_time(self):
        """Метод для заполнения и отображения дат бронирования."""
        dates = self.generate_booking_dates()
        self.bookingdates = BookingRequestCheckDates(**dates)

    @classmethod
    def booking_data(cls):
        """Создание данных букинга"""
        return {
            "firstname": None, #fake.first_name(),
            "lastname": fake.last_name(),
            "totalprice": fake.random_int(min=100, max=10000),
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-04-05",
                "checkout": "2024-04-08"
            },
           "additionalneeds": "Breakfast"
         }

if __name__ == "__main__": # Проверочный пример
    request_data = BookingRequestData.booking_data()
    print(request_data)  # Запускаем заполнение дат бронирования