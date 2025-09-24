
import pytest
from pydantic import BaseModel, ValidationError
from requests import Response
from typing import Type, List, Optional
from src.data_models.project_data_all_bookings import Bookings

class Bookings(BaseModel):
    bookingid: int

def validate_booking_list(
    response: Response,
    model: Type[Bookings],
    expected_status: int = 200,
    expected_data: Optional[List[dict]] = None
) -> List[Bookings]:

    # Проверка статуса ответа
    if response.status_code != expected_status:
        pytest.fail(f"Expected status {expected_status}, got {response.status_code}: {response.text}")

    # Попытка парсинга JSON
    try:
        data = response.json()
    except Exception as e:
        pytest.fail(f"Ошибка парсинга JSON: {e}\nResponse: {response.text}")

    # Проверка, что данные являются списком
    if not isinstance(data, list):
        pytest.fail(f"Ожидался список, получен: {type(data).__name__}")

    # Валидация каждого объекта в списке
    parsed_bookings = []
    for item in data:
        try:
            parsed = model(**item)
            parsed_bookings.append(parsed)
        except ValidationError as e:
            pytest.fail(f"Pydantic валидация не прошла для элемента {item}:\n{e}")

    # Сравнение с ожидаемыми данными
    if expected_data:
        expected_models = [model(**expected_item) for expected_item in expected_data]
        if [booking.model_dump(exclude_unset=True) for booking in parsed_bookings] != [expected_booking.model_dump(exclude_unset=True) for expected_booking in expected_models]:
            pytest.fail(
                f"Данные ответа не совпадают с ожидаемыми:\n"
                f"Expected: {[expected_booking.model_dump() for expected_booking in expected_models]}\n"
                f"Actual:   {[booking.model_dump() for booking in parsed_bookings]}"
            )

    return parsed_bookings




def validate_dates(
    response: Response,
    model: Type[Bookings],
    expected_status: int = 200,
    expected_data: dict | None = None
) -> BaseModel:

    if response.status_code != expected_status:
        pytest.fail(f"Expected status {expected_status}, got {response.status_code}: {response.text}")

    try:
        data = response.json()
    except Exception as e:
        pytest.fail(f"Ошибка парсинга JSON: {e}\nResponse: {response.text}")

    try:
        parsed = model(**data)
    except ValidationError as e:
        pytest.fail(f"Pydantic валидация не прошла:\n{e}")

    if expected_data:
        expected_model = model(**expected_data)
        if parsed.model_dump(exclude_unset=True) != expected_model.model_dump(exclude_unset=True):
            pytest.fail(
                f"Данные ответа не совпадают с ожидаемыми:\n"
                f"Expected: {expected_model.model_dump()}\n"
                f"Actual:   {parsed.model_dump()}"
            )

    print(parsed)
    return parsed
