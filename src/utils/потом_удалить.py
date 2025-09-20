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

class Person:
    def __init__(self, name, age):
        self._name = name       # Защищённое поле
        self.__age = age        # Приватное поле

    def get_age(self):
        return self.__age       # Геттер для возраста

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age   # Сеттер проверяет условие перед изменением значения
        else:
            raise ValueError("Возраст должен быть положительным")

p = Person("Иван", 30)
print(p.get_age())           # Получаем возраст через геттер
p.set_age(35)                # Устанавливаем новый возраст через сеттер
print(p.get_age())
