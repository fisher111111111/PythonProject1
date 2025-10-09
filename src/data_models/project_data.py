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

    @classmethod
    def fake_checkdates(cls) -> "BookingCheckDates":
        start_date = fake.date_between(start_date="today", end_date="+1m")
        end_date = start_date + timedelta(days=random.randint(1, 10))
        return cls(
            checkin= start_date.strftime('%Y-%m-%d'),
            checkout= end_date.strftime('%Y-%m-%d')
        )

class BookingResponseData(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingCheckDates
    additionalneeds: Optional[str] = None

    """ Функции для генерации тестовых данных"""
    @classmethod
    def fake_booking_data(cls) -> "BookingResponseData":
        obj = cls(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            totalprice= fake.random_int(min=100, max=10000),
            depositpaid= fake.boolean(),
            bookingdates= BookingCheckDates.fake_checkdates(),
            additionalneeds=fake.random_element(elements=("breakfast", "dinner", "supper", None))
        )
        return obj.model_dump()

    @classmethod
    def fake_upd_booking_data(cls) -> "BookingResponseData":
        obj = cls(
            firstname="Updately",
            lastname= "Updatenberg",
            totalprice=fake.random_int(min=100, max=10000),
            depositpaid=fake.boolean(),
            bookingdates=BookingCheckDates.fake_checkdates(),
            additionalneeds=fake.random_element(elements=("breakfast", "dinner", "supper", None))
        )
        return obj.model_dump()

    @classmethod
    def fake_patch_booking_data(cls) -> "BookingResponseData":
        obj = cls(
            firstname="Patchey",
            lastname= "Patchison",
            totalprice=fake.random_int(min=100, max=10000),
            depositpaid=fake.boolean(),
            bookingdates=BookingCheckDates.fake_checkdates(),
            additionalneeds=fake.random_element(elements=("breakfast", "dinner", "supper", None))
        )
        return obj.model_dump(include={"firstname", "lastname"})

""" Класс генерации невалидных данных"""
class BookingWrongData(BaseModel):
    firstname: int = 123
    lastname: int = 456
    totalprice: str = "non integer"
    depositpaid: bool = Field(default_factory=fake.boolean)
    bookingdates: BookingCheckDates = Field(default_factory=BookingCheckDates.fake_checkdates)
    additionalneeds: str | None = Field(
        default_factory=lambda: fake.random_element(elements=("breakfast", "dinner", "supper", None)))

    @classmethod
    def fake_wrong_booking_data(cls):
        obj = cls(
            firstname= 123,
            lastname= 456,
            totalprice="string",
            depositpaid=fake.boolean(),
            bookingdates=BookingCheckDates.fake_checkdates(),
            additionalneeds=fake.random_element(elements=("breakfast", "dinner", "supper", None))
        )
        return obj.model_dump()

""" Класс для генерации авторизации """

class BookingAuthData:
    def make_auth_data(self):
        """Создаем и возвращаем данные для авторизации """
        auth_data = os.getenv("VALID_USERNAME"), os.getenv("VALID_PASSWORD")
        return auth_data

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