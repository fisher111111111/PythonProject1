from src.enums.constant_of_url import ConstURL
from src.enums.constant_of_headers import ConstHeaders
from src.data_models.project_data import BookingAuthData, GenerateDates
import requests
from requests.auth import HTTPBasicAuth

class BookingApiClient:
    def __init__(self, booking_session):
        self.booking_session = booking_session
        self.base_url = ConstURL.BASE_URL.value
        self.booking = ConstURL.BOOKING_ENDPOINT.value
        self.headers = ConstHeaders.HEADERS.value
        self.content_type = ConstHeaders.CONTENT_TYPE.value
        self.accept_type = ConstHeaders.ACCEPT.value
        self.auth_data = BookingAuthData().make_auth_data()
        self.auth_obj = HTTPBasicAuth(self.auth_data["username"], self.auth_data["password"])
        self.generator = GenerateDates()

    def create_booking(self):
        '''  Отправляет запрос на создание букинга. '''
        booking_data = self.generator.booking_data()
        response = self.booking_session.post(f"{self.base_url}{self.booking}",
                                             headers = self.headers,
                                             json=booking_data)
        if response.status_code != 200:
            response.raise_for_status()
        response_data = response.json()
        return response_data

    def get_booking(self, booking_id):
        '''
        Отправляет запрос на получение ID конкретного букинга
        '''
        response = self.booking_session.get(f"{self.base_url}{self.booking}/{booking_id}")
        if response.status_code != 200:
            response.raise_for_status()
        json_data = response.json()
        return json_data

    def update_booking(self, booking_id, upd_booking_data):
        '''
        Отправляет запрос на полное обновление букинга
        '''

        response = self.booking_session.put(
            f"{self.base_url}{self.booking}/{booking_id}", json=upd_booking_data,
                                                           headers=self.headers,
                                                           auth=self.auth_obj)
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()

    def patch_booking(self,booking_id, patch_booking_data):
        '''
        Отправляет запрос на частичное обновление букинга
        '''
        response = self.booking_session.patch(f"{self.base_url}{self.booking}/{booking_id}",
            json=patch_booking_data,
            auth=self.auth_obj)
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()

    def get_all_bookings(self):
        '''
        Отправляет запрос на получение всех букингов.
        '''
        response = self.booking_session.get(f"{self.base_url}{self.booking}")
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()

    def delete_booking(self, booking_id):
        '''
        Отправляет запрос на удаление букинга.
        '''
        response = self.booking_session.delete(f"{self.base_url}{self.booking}/{booking_id}",
                     headers=self.headers,
                     auth=self.auth_obj)
        if response.status_code != 201:
            response.raise_for_status()
        return response.status_code, response.text
