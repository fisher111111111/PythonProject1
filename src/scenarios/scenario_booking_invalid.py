import requests
from PythonProject1.src.api.api_manager import BookingApiClient
from  PythonProject1.src.data_models.project_data import BookingResponseData

class BadBookingScenarios:
    def __init__(self, auth_session, api_client: BookingApiClient):
        self.auth_session = auth_session
        self.api_client = api_client
        self.generate_dates = BookingResponseData()

    def bad_create_booking(self):
        '''
        Сценарий 1: Попытка создать букинг с пустыми полями'''
        # 1. Создать букинг
        response = self.booking_session.post(f"{self.base_url}{self.booking}/{booking_id}",
                                             json=None,
                                             headers=self.headers)
        return response.status_code, response.text

    def check_after_delete_booking(self):
        '''
        Сценарий 2: создание букинга, затем удаление букинга и попытка получения
         удаленого букинга по ID '''
        # 1. Создать букинг
        create_book = self.api_client.create_booking()
        booking_id = create_book.get("bookingid")
        print("Создан booking_id =", booking_id)

        # 2. Удалить букинг
        self.api_client.delete_booking(booking_id)
        print(f"booking с ID {booking_id} успешно удален.")
        return booking_id

        #3 Получить удаленный букинг по ID
        get_del_booking = self.api_client.get_booking()
        if (200 <= get_del_booking.status_code <= 299):
            print('букинг получен по удаленному ID, что не ожидалось')
        else:
            print(f"Получен ожидаемый статус код {get_del_booking.status_code}")

    def del_booking_and_try_del_again(self):
        '''
        Сценарий 3: создать и удалить существующий букинг,
        попытаться повторно удалить.
        '''
        # 1. Создать букинг
        create_book = self.api_client.create_booking()
        booking_id = create_book.get("bookingid")
        print("Создан booking_id =", booking_id)

        # 2. Удалить букинг
        del_response = self.api_client.delete_booking(booking_id)
        print(f"booking с ID {booking_id} отправлен на удаление.")
        print(f'букинг {booking_id} удален, что подтверждает ответ сервера {del_response}')

        # 3. Попытка повторного удаления букинга
        repeat_delete_response = del_response
        if (200 <= repeat_delete_response.status_code <= 299):
            print('букинг повторно удален, что не ожидалось')
        else:
            print(f"Повторное удаление букинга с ID {booking_id} завершилось с кодом {repeat_delete_response.status_code}")

    def update_booking_no_auth(self, booking_id, upd_booking_data):
        '''
        Сценарий 4: Отправляет запрос на полное обновление букинга без авторизации
        '''
        response = self.booking_session.put(f"{self.base_url}{self.booking}/{booking_id}",
                                                           auth= None,
                                                           json=upd_booking_data,
                                                           headers=self.headers)
        return response.status_code,response.text

    def patch_booking_no_auth(self,booking_id, patch_booking_data):
        '''
        Сценарий 5: Отправляет запрос на частичное обновление букинга без авторизации
        '''
        response = self.booking_session.patch(f"{self.base_url}{self.booking}/{booking_id}",
                                                             auth=None,
                                                             headers=self.headers,
                                                             json=patch_booking_data)
        return response.status_code,response.text

    def delete_booking_no_auth(self, booking_id):
        '''
        Сценарий 6: Отправляет запрос на удаление букинга без авторизации
        '''
        response = self.booking_session.delete(f"{self.base_url}{self.booking}/{booking_id}",
                                                              auth=None,
                                                              headers=self.headers)
        return response.status_code, response.text
