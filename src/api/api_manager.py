
import  requests
from src.enums.constant_of_url import ConstURL
from src.enums.constant_of_headers import ConstHeaders
from conftest import booking_data, upd_booking_data, bookingid, patch_booking_data, make_auth_data

class BookingApiClient:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = ConstURL.BASE_URL.value  # Можно также передавать в конструктор, если он может меняться
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
        # print("Create_booking", response.json()) #Раскомментить для проверки содержимого в консоли!
        return response_data

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     client = BookingApiClient(auth_session)
#     client.create_booking(booking_data())

    def get_booking(self, bookingid):
        '''
        Отправляет запрос на получение ID конкретного букинга
        '''
        response = self.auth_session.get(f"{self.base_url}/booking/{bookingid}")
        if response.status_code != 200:
            response.raise_for_status()
        json_data = response.json()
        # print(bookingid)
        # print(json_data)
        return json_data

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     client = BookingApiClient(auth_session)
#     client.get_booking(bookingid)
#     print(f"Получаем тело созданного ID {bookingid}")

    def update_booking(self, bookingid, upd_booking_data):
        '''
        Отправляет запрос на обновление букинга
        '''
        auth_data = make_auth_data()
        response = self.auth_session.put(
            f"{self.base_url}/booking/{bookingid}",
            json=upd_booking_data,
            headers=self.base_headers,
            auth=(auth_data['username'], auth_data['password']))
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     client = BookingApiClient(auth_session)
#     client.update_booking(bookingid, upd_booking_data())
#     new_upd_booking = client.update_booking(bookingid, upd_booking_data())
#     print(new_upd_booking)


    def patch_booking(self,bookingid, patch_booking_data):
        '''
        Отправляет запрос на частичное обновление букинга
        '''
        auth_data = make_auth_data()
        response = self.auth_session.patch(f"{self.base_url}/booking/{bookingid}",
            json=patch_booking_data,
            auth=(auth_data['username'], auth_data['password']))
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     client = BookingApiClient(auth_session)
#     client.patch_booking(bookingid, patch_booking_data())
#     new_patch_booking = client.patch_booking(bookingid, patch_booking_data())
#     print(new_patch_booking)


    def get_all_bookings(self):
        '''
        Отправляет запрос на удаление букинга.
        '''
        response = self.auth_session.get(f"{self.base_url}/booking")
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()
#
# if __name__ == "__main__":
#     auth_session = requests.Session()
#     client = BookingApiClient(auth_session)
#     client.get_all_bookings()
#     bookings = client.get_all_bookings()
#     print(bookings)

    def delete_booking(self, bookingid):
        '''
        Отправляет запрос на удаление букинга.
        '''
        auth_data = make_auth_data()
        response = (self.auth_session.delete
                    (f"{self.base_url}/booking/{bookingid}",
                     headers=self.base_headers,
                     auth=(auth_data['username'], auth_data['password'])))
        if response.status_code != 201:
            response.raise_for_status()
        return response.status_code, response.text

# if __name__ == "__main__":
#     auth_session = requests.Session()
#     client = BookingApiClient(auth_session)
#     status_code, text = client.delete_booking(bookingid)
#     print(status_code)
#     print(text)
#     print(f"Удален выбранный букинг = {bookingid}")
