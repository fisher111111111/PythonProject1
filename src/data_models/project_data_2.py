from datetime import timedelta
from pydantic import BaseModel, Field
from typing import Optional
import random
from faker import Faker
import os
from dotenv import load_dotenv

load_dotenv()

fake = Faker()

class BookingAuthData:
    def make_auth_data(self):
        """Создаем и возвращаем данные для переиспользования """
        return {
            "username": os.getenv("VALID_USERNAME"),
            "password": os.getenv("VALID_PASSWORD")
        }

# if __name__ == "__main__":  # Проверка содержания отправляемого тела запроса
#     auth = BookingAuthData()
#     auth_data = auth.make_auth_data()
#     print(auth_data)


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

# if __name__ == "__main__":  # Проверка содержания отправляемого тела запроса
#     req = GenerateDates()
#     request_data = req.booking_data()
#     print(request_data)

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
