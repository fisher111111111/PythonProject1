from src.enums.constant_of_url import ConstURL
from src.enums.constant_of_headers import ConstHeaders
from src.data_models.project_data_2 import BookingAuthData
from src.data_models.project_data_2 import BookingRequestData
import requests

class BookingApiClient:
    def __init__(self, booking_session):
        self.booking_session = booking_session
        self.base_url = ConstURL.BASE_URL.value
        self.booking = ConstURL.BOOKING_ENDPOINT.value
        self.headers = ConstHeaders.HEADERS.value
        self.content_type = ConstHeaders.CONTENT_TYPE.value
        self.accept_type = ConstHeaders.ACCEPT.value
        self.auth_data = BookingAuthData

    def create_booking(self):
        '''  Отправляет запрос на создание букинга. '''
        booking_data = BookingRequestData.booking_data()
        response = self.booking_session.post(f"{self.base_url}{self.booking}",
                                          json=booking_data)
        if response.status_code not in (200, 201):
            response.raise_for_status()
        response_data = response.json()
        return response_data

# if __name__ == "__main__":
#     booking_session = requests.Session()
#     client = BookingApiClient(booking_session)
#     client.create_booking()
#     print(client.create_booking())

    def get_booking(self, bookingid):
        '''
        Отправляет запрос на получение ID конкретного букинга
        '''
        response = self.booking_session.get(f"{self.base_url}{self.booking}/{bookingid}")
        if response.status_code != 200:
            response.raise_for_status()
        json_data = response.json()
        print(bookingid)
        print(json_data)
        return json_data

if __name__ == "__main__":
    booking_session = requests.Session()
    client = BookingApiClient(booking_session)
    # client.get_booking(bookingid)
    # print(f"Получаем тело созданного ID {bookingid}")
#
#     def update_booking(self, bookingid, upd_booking_data):
#         '''
#         Отправляет запрос на обновление букинга
#         '''
#         # auth_data = make_auth_data()  - исправить
#         response = self.booking_session.put(
#             f"{self.base_url}{self.booking}/{bookingid}",
#             json=upd_booking_data,
#             headers=self.headers,
#             auth=self.auth_data)
#         if response.status_code != 200:
#             response.raise_for_status()
#         return response.json()
#
# # if __name__ == "__main__":
# #     auth_session = requests.Session()
# #     client = BookingApiClient(auth_session)
# #     client.update_booking(bookingid, upd_booking_data())
# #     new_upd_booking = client.update_booking(bookingid, upd_booking_data())
# #     print(new_upd_booking)
# #
# #
# #     def patch_booking(self,bookingid, patch_booking_data):
# #         '''
# #         Отправляет запрос на частичное обновление букинга
# #         '''
# #         auth_data = make_auth_data() - испрпавить
# #         response = self.auth_session.patch(f"{self.base_url}{self.booking}/{bookingid}",
# #             json=patch_booking_data, - исправить
# #             auth=(auth_data['username'], auth_data['password'])) - исправить
# #         if response.status_code != 200:
# #             response.raise_for_status()
# #         return response.json()
# #
# # # if __name__ == "__main__":
# # #     bookingh_session = requests.Session()
# # #     client = BookingApiClient(bookingh_session)
# # #     client.patch_booking(bookingid, patch_booking_data())
# # #     new_patch_booking = client.patch_booking(bookingid, patch_booking_data())
# # #     print(new_patch_booking)
# #
# #
# #     def get_all_bookings(self):
# #         '''
# #         Отправляет запрос на удаление букинга.
# #         '''
# #         response = self.booking_session.get(f"{self.base_url}{self.booking}")
# #         if response.status_code != 200:
# #             response.raise_for_status()
# #         return response.json()
# # #
# # # if __name__ == "__main__":
# # #     bookingh_session = requests.Session()
# # #     client = BookingApiClient(bookingh_session)
# # #     client.get_all_bookings()
# # #     bookings = client.get_all_bookings()
# # #     print(bookings)
# #
# #     def delete_booking(self, bookingid):
# #         '''
# #         Отправляет запрос на удаление букинга.
# #         '''
# #         auth_data = make_auth_data()  - исправить
# #         response = (self.booking_session.delete
# #                     (f"{self.base_url}{self.booking}/{bookingid}",
# #                      headers=self.headers,
# #                      auth=(auth_data['username'], auth_data['password'])))
# #         if response.status_code != 201:
# #             response.raise_for_status()
# #         return response.status_code, response.text
# #
# # # if __name__ == "__main__":
# # #     booking_session = requests.Session()
# # #     client = BookingApiClient(booking_session)
# # #     status_code, text = client.delete_booking(bookingid)
# # #     print(status_code)
# # #     print(text)
# # #     print(f"Удален выбранный букинг = {bookingid}")
