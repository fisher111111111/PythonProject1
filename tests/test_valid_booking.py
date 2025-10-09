from src.utils.urls import URLs
from src.data_models.project_data import BookingResponseData
from src.data_models.project_data_patch import BookingPatchData
from src.data_models.project_data_all_bookings import Bookings
from src.utils.project_data_validator import validate_dates
from src.utils.project_patch_data_validator import validate_patch_dates
from src.utils.project_data_all_bookings_validator import validate_booking_list

class TestBookings:

    def test_create_del_check_booking(self, auth_token, fake_booking_data):
        # Create
        create = auth_token.post(URLs.bookings_endpoint(), json=fake_booking_data)
        assert create.status_code == 200
        booking_id = create.json().get("bookingid")

        # Get + Валидировать и данные, и схему
        response = auth_token.get(URLs.booking_endpoint_id(booking_id))
        assert response.status_code == 200
        validate_dates (response, model=BookingResponseData, expected_data=fake_booking_data)

        # Delete
        delete = auth_token.delete(URLs.booking_endpoint_id(booking_id))
        assert delete.status_code == 201

        #Check delete
        check_delete = auth_token.get(URLs.booking_endpoint_id(booking_id))
        assert check_delete.status_code == 404, f"Букинг с ID {booking_id} не был удален"

    def test_upd_booking(self, auth_token, upd_booking_data, del_booking_id):
        #Update
        update = auth_token.put(URLs.booking_endpoint_id(del_booking_id), json=upd_booking_data)
        assert update.status_code == 200

        # Get + Валидировать и данные, и схему
        response = auth_token.get(URLs.booking_endpoint_id(del_booking_id))
        assert response.status_code == 200
        validate_dates(response, model=BookingResponseData, expected_data=upd_booking_data)

    def test_patch_booking(self, auth_token, patch_booking_data, del_booking_id):
        # Получаем тело букинга, которое будем частично изменять, и с которым предстоит сравнивать
        # что неизменённые поля остались прежними
        response = auth_token.get(URLs.booking_endpoint_id(del_booking_id))
        assert response.status_code == 200
        assert response.text.strip() != "", "Тело ответа пустое"
        booking_data = response.json()

        # Patching
        patch = auth_token.patch(URLs.booking_endpoint_id(del_booking_id), json=patch_booking_data)
        assert patch.status_code == 200

        # Объединяем прежние данные с изменёнными
        checking_data = booking_data.copy()
        checking_data.update(patch_booking_data)

        # Get + Валидировать и данные, и схему
        response = auth_token.get(URLs.booking_endpoint_id(del_booking_id))
        assert response.status_code == 200
        validate_patch_dates(response, model=BookingPatchData, expected_data=patch_booking_data)

        # # Delete
        # delete = auth_token.delete(f"{TestBookings.BASE_URL}/booking/{booking_id}")
        # assert delete.status_code == 201

        # # Patching
        # patch = auth_token.patch(URLs.booking_endpoint_id(get_booking_id), json=patch_booking_data)
        # assert patch.status_code == 200
        #
        # # Get + Валидировать и данные, и схему
        # response = auth_token.get(URLs.booking_endpoint_id(get_booking_id))
        # assert response.status_code == 200
        # validate_patch_dates(response, model=BookingPatchData, expected_data=patch_booking_data)

    def test_check_get_all_booking(self, auth_token, bookingids):
        # Get_all + Валидировать и данные, и схему
        response = auth_token.get(URLs.bookings_endpoint())
        assert len(bookingids) > 0, "Список bookings пуст"
        assert response.status_code == 200
        validate_booking_list (response, model=Bookings, expected_data=bookingids)

