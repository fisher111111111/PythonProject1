from pydantic import BaseModel
from typing import Optional


class BookingCheckDates(BaseModel):
    chekin: str
    chekout: str

class BookingResponseData (BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingCheckDates
    additionalneeds: Optional[str]=None

