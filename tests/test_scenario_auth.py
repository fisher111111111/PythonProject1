
from src.enums.constant_of_headers import ConstHeaders
import allure
class TestAuthScenario:

    @allure.title("Авторизация с валидными данными")
    def test_valid_auth (self, time_ping, auth_check_1):
        valid_auth = auth_check_1.right_create_auth()
        assert valid_auth.status_code == 200, "Ошибочный статус-код"
        try:
            body = valid_auth.json()
            assert isinstance(body['token'], str), "Тип токена некорректен"
            assert len(body['token'].strip()) > 0, "Значение Токена пустое"
        except KeyError:
            raise AssertionError("Ключа 'token' нет ответе")
        except ValueError:
            raise AssertionError("Ответ не является JSON")
        assert valid_auth.headers["Content-Type"] == ConstHeaders.CONTENT_TYPE_AUTH.value, "Ошибка в headers.Content-Type ответа"
        assert valid_auth.headers["Content-Length"] == str(len(valid_auth.text)), "Ошибка: headers.Content-Length != длине тела ответа "
        assert time_ping <= ConstHeaders.MAX_TIME_PING.value, f"Время ответа = {time_ping:.2f} секунд, что превышает лимит ({ConstHeaders.MAX_TIME_PING.value:.2f})"

    @allure.title("Авторизация с невалидными данными")
    def test_invalid_auth (self, time_ping, auth_check_1):
        invalid_auth = auth_check_1.wrong_create_auth()
        assert invalid_auth.status_code == 200, "Ошибочный статус-код"
        assert invalid_auth.text == '{"reason":"Bad credentials"}', "Ошибка в теле ответа"
        assert invalid_auth.headers["Content-Type"] == ConstHeaders.CONTENT_TYPE_AUTH.value, "Ошибка в headers.Content-Type ответа"
        assert invalid_auth.headers["Content-Length"] == str(len(invalid_auth.text)), "Ошибка: headers.Content-Length != длине тела ответа "
        assert time_ping <= ConstHeaders.MAX_TIME_PING.value, f"Время ответа = {time_ping:.2f} секунд, что превышает лимит ({ConstHeaders.MAX_TIME_PING.value:.2f})"
