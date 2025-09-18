import pytest
from pydantic import BaseModel, ValidationError
from requests import Response
from typing import Type
from src.data_models.project_data import BookingCheckDates

def validate_check_dates(
    response: Response,
    model: Type[BookingCheckDates],
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
