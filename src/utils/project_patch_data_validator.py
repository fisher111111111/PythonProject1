import pytest
from pydantic import ValidationError
from requests import Response
from typing import Type, Optional
from src.data_models.project_data_patch import BookingPatchData

def validate_patch_dates(
    response: Response,
    model: Type[BookingPatchData],
    expected_status: int = 200,
    expected_data: Optional[dict] = None
) -> BookingPatchData:

    # проверяем, соответствует ли полученный статус-кода ожидаемому значению.
    if response.status_code != expected_status:
        pytest.fail(f"Expected status {expected_status}, got {response.status_code}: {response.text}")

    # преобразовываем тело ответа в Python словарь с использованием метода .json().
    try:
        data = response.json()
    except Exception as e:
        pytest.fail(f"Ошибка парсинга JSON: {e}\\nResponse: {response.text}")

    # при успешном парсинге, полученные данные передаются в модель Pydantic для проверки
    # валидности структуры
    try:
        parsed = model(**data)
    except ValidationError as e:
        pytest.fail(f"Pydantic валидация не прошла:\\n{e}")

    # Если были переданы дополнительные ожидаемые значения (expected_data), функция сравнивает
    # конкретные поля полученной модели с указанными ожиданиями. Для каждого поля выполняется проверка:
    #    - Простые типы данных (строки, числа и т.п.) проверяются напрямую.
    #    - Сложные объекты (вложенные структуры) проверяются рекурсивно.
    #      Если хотя бы одно поле отличается от ожидаемого, создается отчёт о несоответствии с детализацией проблемного поля.
    if expected_data is not None:
        # Создание временной модели только с нужными полями
        class PatchModel(model):
            pass

        # Добавляем только необходимые поля
        for field_name, field_type in expected_data.items():
            setattr(PatchModel, field_name, field_type)

        # Создаем временную модель
        partial_expected_model = PatchModel(**expected_data)

        # Проверяем только те поля, которые заданы в expected_data
        for field_name, expected_value in expected_data.items():
            actual_value = getattr(parsed, field_name)

            if isinstance(expected_value, dict):
                # Рекурсивная проверка вложенных объектов
                for nested_field_name, nested_expected_value in expected_value.items():
                    nested_actual_value = getattr(actual_value, nested_field_name)
                    if nested_actual_value != nested_expected_value:
                        pytest.fail(
                            f"Вложенное поле '{field_name}.{nested_field_name}' отличается от ожидаемого.\\n"
                            f"Expected: {nested_expected_value}\\n"
                            f"Actual:   {nested_actual_value}"
                        )
            elif actual_value != expected_value:
                pytest.fail(
                    f"Поле '{field_name}' отличается от ожидаемого.\\n"
                    f"Expected: {expected_value}\\n"
                    f"Actual:   {actual_value}"
                )

    return parsed