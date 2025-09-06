
import  requests
from src.enums.constant_of_url import ConstURL
from src.enums.constant_of_headers import ConstHeaders
from conftest import booking_data, upd_booking_data, bookingid, patch_booking_data, make_auth_data, non_auth_data

class BadBookingApiClient:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = ConstURL.BASE_URL.value
        self.base_headers = ConstHeaders.HEADERS.value

    def create_booking(self, booking_data):
        '''
        Отправляет запрос на создание букинга.
        '''
        response = self.auth_session.post(f"{self.base_url}/booking",
                                          json=booking_data)
        if response.status_code not in (200, 201):
            response.raise_for_status()
        response_data = response.json()
        return response_data

#проверка содержимого ответа
# if __name__ == "__main__":
#     auth_session = requests.Session()  # или ваша сессия с авторизацией
#     client = BadBookingApiClient(auth_session)
#     a = client.create_booking(booking_data())
#     print(a)

    def wrong_update_booking(self, bookingid, upd_booking_data):
        '''
        Отправляет запрос на обновление букинга
        '''
        auth_data = non_auth_data()
        response = self.auth_session.put(
            f"{self.base_url}/booking/{bookingid}",
            json=upd_booking_data,
            headers=self.base_headers,
            auth=(auth_data['username'], auth_data['password']))
        if response.status_code != 403:
            print(f'Получен неожидаемый статус код -{response.status_code}')
        return response.status_code

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     client = BadBookingApiClient(auth_session)
#     client.wrong_update_booking(bookingid, upd_booking_data())
#     status_booking = client.wrong_update_booking(bookingid, upd_booking_data())
#     print(f'получен ожидаемый статус код {status_booking}')


    def wrong_patch_booking(self,bookingid, patch_booking_data):
        '''
        Отправляет запрос на частичное обновление букинга
        '''
        auth_data = non_auth_data()
        response = self.auth_session.patch(f"{self.base_url}/booking/{bookingid}",
            json=patch_booking_data,
            auth=(auth_data['username'], auth_data['password']))
        if response.status_code != 403:
            print(f'Получен неожидаемый статус код -{response.status_code}')
        return response.status_code

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     client = BadBookingApiClient(auth_session)
#     client.wrong_patch_booking(bookingid, patch_booking_data())
#     new_upd_booking = client.wrong_patch_booking(bookingid, patch_booking_data())
#     print(f'получен ожидаемый статус код {new_upd_booking}')

    def wrong_delete_booking(self, bookingid):
        '''
        Отправляет запрос на удаление букинга.
        '''
        auth_data = non_auth_data()
        response = (self.auth_session.delete
                    (f"{self.base_url}/booking/{bookingid}",
                     headers=self.base_headers,
                     auth=(auth_data['username'], auth_data['password'])))
        if response.status_code != 403:
            print(f'Получен неожидаемый статус код -{response.status_code}')
        return response.status_code

if __name__ == "__main__":
    auth_session = requests.Session()
    client = BadBookingApiClient(auth_session)
    client.wrong_delete_booking(bookingid)
    status_booking = client.wrong_delete_booking(bookingid)
    print(f'получен ожидаемый статус код {status_booking}')
