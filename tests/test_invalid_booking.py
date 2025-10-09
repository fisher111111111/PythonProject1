from src.utils.urls import URLs
from src.enums.constant_of_url import ConstURL
from src.data_models.project_data import BookingResponseData
from src.utils.project_data_validator import validate_dates

class TestBookings:

    def test_create_wrong_booking(self, auth_token, fake_wrong_booking_data):
        # Create
        create = auth_token.post(URLs.bookings_endpoint(), json=fake_wrong_booking_data)
        assert create.status_code == 500

    def test_upd_booking(self, auth_token, fake_booking_data, upd_booking_data, del_booking_id):

        # Create
        create = auth_token.post(URLs.bookings_endpoint(), json=fake_booking_data)
        assert create.status_code == 200
        booking_id = create.json().get("bookingid")

        #Update
        update = auth_token.put(URLs.booking_endpoint_id(booking_id), json=upd_booking_data)
        assert update.status_code == 200

        # Delete
        delete = auth_token.delete(URLs.booking_endpoint_id(booking_id))
        assert delete.status_code == 201

        #Check delete
        check_delete = auth_token.get(URLs.booking_endpoint_id(booking_id))
        assert check_delete.status_code == 404, f"Букинг с ID {booking_id} не был удален"

    def test_patch_booking(self, auth_token, fake_booking_data, patch_booking_data, del_booking_id):
        # Активируем del_booking_id
        a = del_booking_id

        # Create
        create = auth_token.post(URLs.bookings_endpoint(), json=fake_booking_data)
        assert create.status_code == 200
        booking_id = create.json().get("bookingid")

        # Patching
        patch = auth_token.patch(URLs.booking_endpoint_id(booking_id), json=patch_booking_data)
        assert patch.status_code == 200

        # Delete
        delete = auth_token.delete(URLs.booking_endpoint_id(booking_id))
        assert delete.status_code == 201

        # Check delete
        check_delete = auth_token.delete(URLs.booking_endpoint_id(booking_id))
        assert check_delete.status_code == 405, f"Букинг с ID {booking_id} не был удален"

