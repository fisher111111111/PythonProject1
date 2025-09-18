from enum import Enum

class ConstHeaders(Enum):
    HEADERS = {"Content-Type":"application/json", "Accept":"application/json"}
    CONTENT_TYPE = 'application/json'
    ACCEPT = 'application/json'
    COOKIES = "token=abc123"
    CONTENT_TYPE_PING = "text/plain; charset=utf-8"
    CONTENT_TYPE_AUTH = "application/json; charset=utf-8"
    MAX_TIME_PING = 0.01   # Максимально допустимое время ответа в миллисекундах