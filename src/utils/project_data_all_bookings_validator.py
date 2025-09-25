
import pytest
from pydantic import BaseModel, ValidationError
from requests import Response
from typing import Type, List, Optional
from src.data_models.project_data_all_bookings import Bookings

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
        if expected_data:
            actual_ids = {booking['bookingid'] for booking in data}
            expected_ids = {booking['bookingid'] for booking in expected_data}
            if not expected_ids.issubset(actual_ids):
                pytest.fail(f"В ответе отсутствуют ожидаемые bookingid: {expected_ids - actual_ids}")
    except Exception as e:
        pytest.fail(f"Ошибка парсинга JSON: {e}\nResponse: {response.text}")

    # Проверка, что данные являются списком
    if not isinstance(data, list):
        pytest.fail(f"Ожидаемый список не получен. Получено: {type(data.text)}")

    # Валидация каждого объекта в списке
    parsed_bookings = []
    for booking in data:
        try:
            parsed = model(**booking)
            parsed_bookings.append(parsed)
        except ValidationError as e:
            pytest.fail(f"Pydantic валидация не прошла для элемента {booking}:\n{e}")

    # Сравнение наличия созданного букинга в общем списке букингов
    if expected_data:
        expected_models = [model(**expected_item) for expected_item in expected_data]
        if not (expected_model in parsed_bookings for expected_model in expected_models):
            pytest.fail(
                f"Данные ответа не совпадают с ожидаемыми:\n"
                f"Expected: {[expected_models]}\n"
                f"Actual:   {[parsed_bookings]}"
            )

    return parsed_bookings
