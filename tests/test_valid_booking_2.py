
from src.enums.constant_of_url import ConstURL
from src.data_models.project_data import BookingResponseData
from src.data_models.project_data_all_bookings import Bookings
from src.utils.project_data_validator import validate_dates
from src.utils.project_data_all_bookings_validator import validate_booking_list

class TestBookings:

    BASE_URL = ConstURL.BASE_URL.value

    def test_create_del_check_booking(self, auth_token, booking_data):
        # Create
        create = auth_token.post(f"{TestBookings.BASE_URL}/booking", json=booking_data)
        assert create.status_code == 200
        booking_id = create.json().get("bookingid")

        # Get + Валидировать и данные, и схему
        response = auth_token.get(f"{TestBookings.BASE_URL}/booking/{booking_id}")
        validate_dates (response, model=BookingResponseData, expected_data=booking_data)

        # Delete
        delete = auth_token.delete(f"{TestBookings.BASE_URL}/booking/{booking_id}")
        assert delete.status_code == 201

        #Check delete
        check_delete = auth_token.get(f"{TestBookings.BASE_URL}/booking/{booking_id}")
        assert check_delete.status_code == 404, f"Букинг с ID {booking_id} не был удален"

    def test_upd_booking(self, auth_token, get_booking_id, upd_booking_data, del_booking_id):
        #Update
        update = auth_token.put(f"{TestBookings.BASE_URL}/booking/{get_booking_id}", json=upd_booking_data)
        assert update.status_code == 200

        # Get + Валидировать и данные, и схему
        response = auth_token.get(f"{TestBookings.BASE_URL}/booking/{get_booking_id}")
        validate_dates(response, model=BookingResponseData, expected_data=upd_booking_data)

    def test_patch_booking(self, auth_token, booking_data, patch_booking_data, del_booking_id):
        create = auth_token.post(f"{TestBookings.BASE_URL}/booking", json=booking_data)
        assert create.status_code == 200
        booking_id = create.json().get("bookingid")
        # Patching

        patch = auth_token.patch(f"{TestBookings.BASE_URL}/booking/{booking_id}", json=patch_booking_data)
        assert patch.status_code == 200

        # Объединяем прежние данные с изменёнными
        checking_data = booking_data.copy()
        checking_data.update(patch_booking_data)

        # Get + Валидировать и данные, и схему
        response = auth_token.get(f"{TestBookings.BASE_URL}/booking/{booking_id}")
        print (response)
        validate_dates(response, model=BookingResponseData, expected_data=checking_data)


    # def test_patch_booking(self, auth_token, get_booking_id, patch_booking_data, del_booking_id):
    #     create = auth_token.post(f"{TestBookings.BASE_URL}/booking", json=booking_data)
    #     assert create.status_code == 200
    #     booking_id = create.json().get("bookingid")
    #     # Patching
    #     patch = auth_token.patch(f"{TestBookings.BASE_URL}/booking/{get_booking_id}", json=patch_booking_data)
    #     assert patch.status_code == 200
    #
    #     # Объединяем прежние данные с изменёнными
    #     checking_data = get_booking_id.copy()
    #     checking_data.update(patch_booking_data)
    #
    #     # Get + Валидировать и данные, и схему
    #     response = auth_token.get(f"{TestBookings.BASE_URL}/booking/{get_booking_id}")
    #     validate_dates(response, model=BookingResponseData, expected_data=checking_data)

    def test_check_get_all_booking(self, auth_token, get_booking_id, bookingids, del_booking_id):
        # Get_all + Валидировать и данные, и схему
        response = auth_token.get(f"{TestBookings.BASE_URL}/booking")
        validate_booking_list (response, model=Bookings, expected_data=bookingids)

