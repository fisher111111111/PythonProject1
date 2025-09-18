from pydantic import BaseModel
from typing import Optional


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

