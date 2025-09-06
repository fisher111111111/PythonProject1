# import requests
#
# from conftest import booking_data
# from src.api.api_manager import BookingApiClient
#
# class bookingScenarios:
#     def __init__(self, api_client: BookingApiClient):  # Типизация для ясности
#         self.api_client = api_client
#
#     def create_check_delete_booking(self):
#         """
#         Сценарий: создать booking и сразу же его удалить.
#         Возвращает ID созданного и удаленного booking.
#         """
#         self.api_client.delete_booking(booking_data)  # Проверка на успешность удаления внутри delete_booking (raise_for_status)
#         # или можно проверить статус ответа здесь, если delete_booking его возвращает
#         print(f"booking с ID {booking_id} успешно создан и удален.")
#         return booking_id
#
# if __name__ == "__main__":
#     # auth_session = requests.Session()
#     api_client = BookingApiClient()
#     client = bookingScenarios(api_client)
#     booking_id = client.create_check_delete_booking()

    # def get_and_verify_bookings_exist(self):
    #     """
    #     Сценарий: получить список bookings и проверить, что он не пуст.
    #     """
    #     bookings = self.api_client.get_bookings()
    #     assert len(bookings) > 0, "Список bookings пуст"
    #     print(f"Получено {len(bookings)} bookings.")
    #     return bookings
    #
    # def update_booking_and_verify_changes(self, booking_id, upd_booking_data):
    #     """
    #     Сценарий: обновить booking и проверить, что данные изменились.
    #     """
    #     updated_booking = self.api_client.update_booking(booking_id, upd_booking_data)
    #
    #     assert updated_booking["description"] == upd_booking_data["description"], \
    #         f"Описание не обновилось. Ожидалось: {upd_booking_data['description']}, получено: {updated_booking['description']}"
    #     assert updated_booking["title"] == upd_booking_data["title"], \
    #         f"Заголовок не обновился. Ожидалось: {upd_booking_data['title']}, получено: {updated_booking['title']}"
    #     print(f"booking с ID {booking_id} успешно обновлен.")
    #     return updated_booking
    #
    # def delete_existing_booking_and_verify(self, booking_id):  # test_booking переименован в booking_id для ясности
    #     """
    #     Сценарий: удалить существующий booking и убедиться, что он удален.
    #     """
    #     self.api_client.delete_booking(booking_id)
    #     print(f"booking с ID {booking_id} отправлен на удаление.")



from conftest import booking_data
from src.api.api_manager import BookingApiClient

class bookingScenarios:
    def __init__(self, api_client: BookingApiClient):
        self.api_client = api_client

    def create_booking_and_immediately_delete(self):
        # 1. Создать бронирование
        create_resp = self.api_client.create_booking(booking_data())
        booking_id = create_resp.get("bookingid")  # обязательно .get или доступ по ключу
        print("Создан booking_id =", booking_id)

        # 2. Убедиться, что получили id
        if booking_id is None:
            raise RuntimeError("Не удалось получить bookingid при создании")

        # 3. Удалить по id
        del_resp = self.api_client.delete_booking(booking_id)
        # del_resp.raise_for_status()  # либо delete_booking уже вызывает raise_for_status
        print(f"booking с ID {booking_id} успешно удален.")
        return booking_id

if __name__ == "__main__":
    api_client = BookingApiClient()
    client = bookingScenarios(api_client)
    booking_id = client.create_booking_and_immediately_delete()
