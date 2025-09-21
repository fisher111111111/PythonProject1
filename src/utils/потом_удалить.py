# # Выводим заголовок таблицы
# print("Таблица умножения:")
# print("   ", end="")  # Пустое пространство для выравнивания
#
# # Заголовок для множителей
# for j in range(1, 11):
#     print(f"{j:4}", end="")  # Выравнивание по ширине
# print()  # Переход на новую строку
#
# # Основной цикл для таблицы умножения
# for i in range(1, 11):
#     print(f"{i:2} |", end="")  # Выводим номер строки
#     for j in range(1, 11):
#         print(f"{i * j:4}", end="")  # Выводим произведение
#     print()  # Переход на новую строку

#
# for j in range(1, 11):
#     print(f"{j:4}", end= "")  # Выравнивание по ширине
#

#
# import pytest
#
# # Параметры сформированы однострочным генератором списка
# params = [(x, x * 2) for x in range(5)]  # [(0,0), (1,2), (2,4), (3,6), (4,8)]
#
# @pytest.mark.parametrize("input_value, expected", params)
# def test_double(input_value, expected):
#     assert input_value * 2 == expected
# pytest.mark.parametrize.mark.name.find()

import re

# Простая регулярка: есть символ @ и хотя бы одна точка после него
EMAIL_RE = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')
qq = re.finditer
def is_valid_email(email: str) -> bool:
    """Возвращает True, если email соответствует шаблону (есть @ и точка после него)."""
    return bool(EMAIL_RE.match(email))

# Примеры
tests = [
    "user@example.com",
    "user.name@sub.domain.ru",
    "user@localhost",      # неверно — нет точки в домене
    "user@@example.com",   # неверно — два @
    "user example@com",    # неверно — пробелы
    "user@.com",           # неверно — пустая часть домена перед точкой
    "1@domen.com"
]

for t in tests:
    print(f"{t:30} -> {is_valid_email(t)}")
