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

class BookingCheckDatesPatch(BaseModel):
    checkin: str
    checkout: str

    @classmethod
    def fake_checkdates(cls) -> "BookingCheckDatesPatch":
        start_date = fake.date_between(start_date="today", end_date="+1m")
        end_date = start_date + timedelta(days=random.randint(1, 10))
        return cls(
            checkin=start_date.strftime('%Y-%m-%d'),
            checkout=end_date.strftime('%Y-%m-%d')
        )

class BookingPatchData(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    totalprice: Optional[int] = None
    depositpaid: Optional[bool] = None
    bookingdates: Optional[BookingCheckDatesPatch] = None
    additionalneeds: Optional[str] = None

    """ Функции для генерации тестовых данных для метода PATCH"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def fake_patch_booking_data(cls) -> "BookingPatchData":
        required_fields = ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates"]
        selected_fields = random.sample(required_fields, random.randint(1, len(required_fields)))

        obj = cls(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            totalprice=fake.random_int(min=100, max=10000),
            depositpaid=fake.boolean(),
            bookingdates=BookingCheckDatesPatch.fake_checkdates(),
            additionalneeds=fake.random_element(elements=("breakfast", "dinner", "supper", None))
        )
        return obj.model_dump(include=selected_fields)
