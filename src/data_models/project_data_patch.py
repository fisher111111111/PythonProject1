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

class BookingPatchData(BaseModel):
    firstname: str = None
    lastname: str = None
    totalprice: int = None
    depositpaid: bool = None
    bookingdates: BookingCheckDates = None
    additionalneeds: Optional[str] = None

    """ Функции для генерации тестовых данных для метода PATCH"""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def model_dump(self, include=None):
        if include is not None:
            return {k: v for k, v in vars(self).items() if k in include}

    @classmethod
    def fake_patch_booking_data(cls) -> "BookingResponseData":
        required_fields = ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates"]
        selected_fields = random.sample(required_fields, random.randint(1, len(required_fields)))

        obj = cls(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            totalprice=fake.random_int(min=100, max=10000),
            depositpaid=fake.boolean(),
            bookingdates=BookingCheckDates.fake_checkdates(),
            additionalneeds=fake.random_element(elements=("breakfast", "dinner", "supper", None))
        )
        return obj.model_dump(include=selected_fields)

#
#     @classmethod
#     def fake_booking_data(cls) -> "BookingPatchData":
#         obj = cls(
#             firstname=fake.first_name(),
#             lastname=fake.last_name(),
#             totalprice= fake.random_int(min=100, max=10000),
#             depositpaid= fake.boolean(),
#             bookingdates= BookingCheckDates.fake_checkdates(),
#             additionalneeds=fake.random_element(elements=("breakfast", "dinner", "supper", None))
#         )
#         return obj.model_dump()
#
#     @classmethod
#     def fake_upd_booking_data(cls) -> "BookingResponseData":
#         obj = cls(
#             firstname="Updately",
#             lastname= "Updatenberg",
#             totalprice=fake.random_int(min=100, max=10000),
#             depositpaid=fake.boolean(),
#             bookingdates=BookingCheckDates.fake_checkdates(),
#             additionalneeds=fake.random_element(elements=("breakfast", "dinner", "supper", None))
#         )
#         return obj.model_dump()
#
#     @classmethod
#     def fake_patch_booking_data(cls) -> "BookingResponseData":
#         obj = cls(
#             firstname="Patchey",
#             lastname= "Patchison",
#             totalprice=fake.random_int(min=100, max=10000),
#             depositpaid=fake.boolean(),
#             bookingdates=BookingCheckDates.fake_checkdates(),
#             additionalneeds=fake.random_element(elements=("breakfast", "dinner", "supper", None))
#         )
#         return obj.model_dump(include={"firstname", "lastname"})
#
# """ Класс генерации невалидных данных"""
# class BookingWrongData(BaseModel):
#     firstname: int = 123
#     lastname: int = 456
#     totalprice: str = "non integer"
#     depositpaid: bool = Field(default_factory=fake.boolean)
#     bookingdates: BookingCheckDates = Field(default_factory=BookingCheckDates.fake_checkdates)
#     additionalneeds: str | None = Field(
#         default_factory=lambda: fake.random_element(elements=("breakfast", "dinner", "supper", None)))
#
#     @classmethod
#     def fake_wrong_booking_data(cls):
#         obj = cls(
#             firstname= 123,
#             lastname= 456,
#             totalprice="string",
#             depositpaid=fake.boolean(),
#             bookingdates=BookingCheckDates.fake_checkdates(),
#             additionalneeds=fake.random_element(elements=("breakfast", "dinner", "supper", None))
#         )
#         return obj.model_dump()
