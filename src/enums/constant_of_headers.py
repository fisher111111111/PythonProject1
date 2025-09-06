from enum import Enum

class ConstHeaders(Enum):
    HEADERS = {"Content-Type":"application/json", "Accept":"application/json", "Cookies": "token=123"}
    CONTENT_TYPE = 'application/json'
    ACCEPT = 'application/json'
    COOKIES = "token=abc123"

headers_dict = dict(ConstHeaders.HEADERS.value)
