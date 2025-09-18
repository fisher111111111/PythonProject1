
import requests
# from conftest import booking_data, upd_booking_data, patch_booking_data
from src.api.api_manager import BookingApiClient

class BookingScenarios:
    def __init__(self, auth_session, api_client: BookingApiClient):
        self.auth_session = auth_session
        self.api_client = api_client

    def create_check_delete_booking(self):
        '''
        Сценарий 1: создание букинга, проdерка ID созданного букинга,
        затем удаление букинга '''
        # 1. Создать букинг
        create_book = self.api_client.create_booking(booking_data()) # вместо booking_data захардкодить прям сюда через Faker
        booking_id = create_book.get("bookingid")
        print("Создан booking_id =", booking_id)

        # 2. Проверить получение созданного букинга
        if booking_id is None:
            raise RuntimeError("Не удалось получить созданный bookingid")
        print("Наличие ID успешно проверено")

        # 3. Удалить букинг
        del_book = self.api_client.delete_booking(booking_id)
        print(f"booking с ID {booking_id} успешно удален.")
        return booking_id

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     api_client = BookingApiClient(auth_session)
#     client = BookingScenarios(auth_session, api_client)
#     booking_id = client.create_check_delete_booking()

    def check_get_booking(self):
        '''
        Cценарий 2: создание букинга, проерка получения букинга по ID
        '''
        # 1. Создать букинг
        create_book = self.api_client.create_booking(booking_data())
        body_booking_id = create_book.get("booking")
        check_booking_id = create_book.get("bookingid")
        print(f'ID созданного букинга = {check_booking_id}')
        print(f'Тело созданного букинга = {body_booking_id}')

        #2. Получить созданный букинг по ID
        get_booking_ID = self.api_client.get_booking(check_booking_id)
        print(f'Тело для сравнения {get_booking_ID}')
        assert body_booking_id == get_booking_ID, "провалено сравнение тел POST и GET запроов с одинаковым ID "
        return get_booking_ID

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     api_client = BookingApiClient(auth_session)
#     client = BookingScenarios(auth_session, api_client)
#     booking_id_list = client.check_get_booking()

    def get_and_verify_bookings_exist(self):
        '''
        Сценарий 3: получить список букингов и проверить, что он не пуст.
        '''
        #1. Получить ссписок ID букмнгов и проверить его наполненность
        bookings = self.api_client.get_all_bookings()
        assert len(bookings) > 0, "Список bookings пуст"
        print(bookings)
        print(f"Получено {len(bookings)} bookings.")
        return bookings

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     api_client = BookingApiClient(auth_session)
#     client = BookingScenarios(auth_session, api_client)
#     booking_id_list = client.get_and_verify_bookings_exist()

    def create_check_in_all_booking(self):
        '''
        Cценарий 4: создать букинг, проерить наличия созданного ID букинга,
        в общем списке, а затем удалить букинг
        '''
        # 1. Создать букинг
        create_book = self.api_client.create_booking(booking_data())
        booking_id = create_book.get("bookingid")
        print("Создан booking_id =", booking_id)

        #2  Получить общий список букингов
        bookings = self.api_client.get_all_bookings()
        assert len(bookings) > 0, "Список bookings пуст"
        print(bookings)
        print(f"Получено {len(bookings)} bookings.")

        #3. Проверить, что созданный букинг есть в списке
        booking_ids = [b.get("bookingid") for b in bookings]
        assert booking_id in booking_ids, "Созданного букинга нет в списке всех букингов"
        print("Созданный букинг действительно находится в списке всех букингов")

        #4.  Удалить букинг
        del_book = self.api_client.delete_booking(booking_id)
        print(f"booking с ID {booking_id} успешно удален.")
        return booking_id

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     api_client = BookingApiClient(auth_session)
#     client = BookingScenarios(auth_session, api_client)
#     booking_id_list = client.create_check_in_all_booking()

    def update_booking_and_verify_changes(self):
        '''
        Cценарий 5: созданиe букинга, изменение всего тела букинга
        '''
        # 1. Создать букинг
        create_book = self.api_client.create_booking(booking_data())
        booking_id = create_book.get("bookingid")
        print("Создан booking_id =", booking_id)

        #2. Изменить букинг
        update_booking_data =  upd_booking_data()
        updated_booking = self.api_client.update_booking(booking_id, update_booking_data)
        assert updated_booking == update_booking_data, f"Букинг не обновился."
        print(f"booking с ID {booking_id} успешно обновлен.")
        return updated_booking

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     api_client = BookingApiClient(auth_session)
#     client = BookingScenarios(auth_session, api_client)
#     booking_id_list = client.update_booking_and_verify_changes()

    def patch_booking_and_verify_changes(self):
        '''
        Cценарий 6: создать букинг, частично обновить в букинге
        только фамилию и имя клиента
        '''
        # 1. Создать букинг
        create_book = self.api_client.create_booking(booking_data())
        booking_id = create_book.get("bookingid")
        print("Создан booking_id =", booking_id)

        #2. Частично изменить букинг
        ptch_booking_data = patch_booking_data()
        patched_booking = self.api_client.patch_booking(booking_id, ptch_booking_data)
        final_patch_booking = {key: patched_booking[key] for key in ['firstname', 'lastname']}
        assert final_patch_booking == ptch_booking_data, f"Букинг частично не обновился."
        print(f"booking с ID {booking_id} c успехом хоть и частично, но обновлен.")
        return final_patch_booking

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     api_client = BookingApiClient(auth_session)
#     client = BookingScenarios(auth_session, api_client)
#     booking_id_list = client.patch_booking_and_verify_changes()

    def delete_existing_booking_and_verify(self):
        '''
        Сценарий 7: создать и удалить существующий букинг,
        убедиться, что он удален из общего списка
        '''
        # 1. Создать букинг
        create_book = self.api_client.create_booking(booking_data())
        booking_id = create_book.get("bookingid")
        print("Создан booking_id =", booking_id)

        #2. Удалить букинг
        self.api_client.delete_booking(booking_id)
        print(f"booking с ID {booking_id} отправлен на удаление.")

        # 3  Получить общий список букингов
        bookings = self.api_client.get_all_bookings()
        assert len(bookings) > 0, "Список bookings пуст"
        print(bookings)

        # 4. Проверить, что созданный букинг есть в списке
        booking_ids = [b.get("bookingid") for b in bookings]
        assert booking_id not in booking_ids, "Удаленный букинг еть в списке всех букингов"
        print("Удаленный букинг отсутствует в списке всех букингов")

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     api_client = BookingApiClient(auth_session)
#     client = BookingScenarios(auth_session, api_client)
#     booking_id_list = client.delete_existing_booking_and_verify()

    def delete_booking_and_try_del_again(self):
        '''
        Сценарий 8: создать и удалить существующий букинг,
        попытаться повторно удалить.
        '''
        # 1. Создать букинг
        create_book = self.api_client.create_booking(booking_data())
        booking_id = create_book.get("bookingid")
        print("Создан booking_id =", booking_id)

        #2. Удалить букинг
        del_response = self.api_client.delete_booking(booking_id)
        print(f"booking с ID {booking_id} отправлен на удаление.")
        print(f'букинг {booking_id} удален, что подтверждает ответ сервера {del_response}')

        #3. Попытка повторного удаления букинга
        try:
            repeat_delete_response = self.api_client.delete_booking(booking_id)
            if (200 <= repeat_delete_response.status_code <= 299):
                print('букинг повторно удален, что не ожидалось')
            else:
                print(
                    f"Повторное удаление букинга с ID {booking_id} завершилось с кодом {repeat_delete_response.status_code}")
        except requests.exceptions.HTTPError as error_del:
            print(f"Ошибка при повторном удалении букинга: {error_del}")
            print(f"букинг с ID {booking_id} повторно не удаляется")

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     api_client = BookingApiClient(auth_session)
#     client = BookingScenarios(auth_session, api_client)
#     booking_id_list = client.delete_booking_and_try_del_again()
