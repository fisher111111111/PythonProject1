import pytest

from src.enums.constant_of_url import ConstURL
from src.data_models.project_data import BookingResponseData
from src.utils.project_resp_data_validator import validate_response_data

class TestBookings:

    BASE_URL = ConstURL.BASE_URL.value


    def test_create_booking(self, auth_token, booking_data):
        # Create
        create = auth_token.post(f"{TestBookings.BASE_URL}/booking", json=booking_data)
        assert create.status_code == 200
        booking_id = create.json().get("bookingid")

        # Get + Валидировать и данные, и схему
        response = auth_token.get(f"{TestBookings.BASE_URL}/booking/{booking_id}")
        validate_response_data (response, model=BookingResponseData, expected_data=booking_data)

        # Delete
        delete = auth_token.delete(f"{TestBookings.BASE_URL}/booking/{booking_id}")
        assert delete.status_code == 201
