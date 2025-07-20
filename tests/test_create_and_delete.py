import pytest

from Module_4_2.conftest import auth_session
from constant_of_url import ConstURL
from project_data import BookingResponseData
from project_resp_data_validator import validate_response_data

class TestBookings:

    BASE_URL = ConstURL.BASE_URL.value
    @pytest.fixture
    def test_create_booking(self, auth_session, booking_data):
        # Create
        create = auth_session.post(f"{TestBookings.BASE_URL}/booking", json=booking_data)
        assert create.status_code == 200
        booking_id = create.json().get("bookingid")

        # Get + Валидировать и данные, и схему
        response = auth_session.get(f"{TestBookings.BASE_URL}/booking/{booking_id}")
        validate_response_data (response, model=BookingResponseData, expected_data=booking_data)

        # Delete
        delete = auth_session.delete(f"{TestBookings.BASE_URL}/booking/{booking_id}")
        assert delete.status_code == 201
