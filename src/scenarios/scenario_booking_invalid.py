
import requests
from src.api.api_manager import BookingApiClient
from  src.data_models.project_data import GenerateDates

class BadBookingScenarios:
    def __init__(self, auth_session, api_client: BookingApiClient):
        self.auth_session = auth_session
        self.api_client = api_client
        self.generate_dates = GenerateDates()

    def bad_create_booking(self):
        '''
        Сценарий 1: Попытка создать букинг без обязательных полей'''
        # 1. Создать букинг
        self.api_client.create_booking()

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     api_client = BookingApiClient(auth_session)
#     client = BookingScenarios(auth_session, api_client)
#     result = client.create_wrong_booking()
#     print(result)

    def bad_update_booking(self):
        '''
        Cценарий 5: созданиe букинга, изменение всего тела букинга
        '''
        # 1. Создать букинг
        create_book = self.api_client.create_booking()
        booking_id = create_book.get("bookingid")
        print(f"Создан букинг {create_book}")

        #2. Изменить букинг без авторизации
        updating_booking_data =  self.generate_dates.upd_booking_data()
        updated_booking = self.api_client.update_booking_no_auth(booking_id, updating_booking_data)
        print(f"При попытке изменить букинг без авторизации получаем {updated_booking}")
        return updated_booking

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     api_client = BookingApiClient(auth_session)
#     client = BadBookingScenarios(auth_session, api_client)
#     booking_id_list = client.bad_update_booking()

    def bad_patch_booking(self):
        '''
        Cценарий 6: создать букинг, частично обновить в букинге
        только фамилию и имя клиента
        '''
        # 1. Создать букинг
        create_book = self.api_client.create_booking()
        booking_id = create_book.get("bookingid")
        print("Создан booking_id =", booking_id)

        #2. Частично изменить букинг
        ptch_booking_data = self.generate_dates.patch_booking_data()
        patched_booking = self.api_client.patch_booking_no_auth(booking_id, ptch_booking_data)
        print(f"При попытке частично обновить букинг без авторизации \nполучен ответ сервера {patched_booking}")
        return patched_booking

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     api_client = BookingApiClient(auth_session)
#     client = BadBookingScenarios(auth_session, api_client)
#     booking_id_list = client.bad_patch_booking()

    def bad_delete_booking(self):
        '''
        Сценарий 7: создать и удалить существующий букинг,
        убедиться, что он удален из общего списка
        '''
        # 1. Создать букинг
        create_book = self.api_client.create_booking()
        booking_id = create_book.get("bookingid")
        print("Создан booking_id =", booking_id)

        #2. Удалить букинг без авторизации
        delete_non_auth = self.api_client.delete_booking_no_auth(booking_id)
        print(f"При попытке удалить букинг без регистрации\nполучен результат {delete_non_auth}")

        # 3. Удалить букинг с авторизацией
        del_response = self.api_client.delete_booking(booking_id)
        print(f'букинг {booking_id} удален, что подтверждает ответ сервера {del_response}')

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     api_client = BookingApiClient(auth_session)
#     client = BadBookingScenarios(auth_session, api_client)
#     booking_id_list = client.bad_delete_booking()
