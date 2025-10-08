
from src.enums.constant_of_headers import ConstHeaders

class TestAuthScenario:

    def test_valid_auth (self, time_ping, auth_check):
        valid_auth = auth_check.right_create_auth()
        assert valid_auth.status_code == 200, "Ошибочный статус-код"
        body = valid_auth.json()
        assert isinstance(body['token'], str), "Тип токена некорректен"
        assert len(body['token'].strip()) > 0, "Значение Токена пустое"
        assert valid_auth.headers["Content-Type"] == ConstHeaders.CONTENT_TYPE_AUTH.value, "Ошибка в headers.Content-Type ответа"
        assert valid_auth.headers["Content-Length"] == str(len(valid_auth.text)), "Ошибка: headers.Content-Length != длине тела ответа "
        assert time_ping <= ConstHeaders.MAX_TIME_PING.value, f"Время ответа = {time_ping:.2f} секунд, что превышает лимит ({ConstHeaders.MAX_TIME_PING.value:.2f})"

    def test_invalid_auth (self, time_ping, auth_check):
        invalid_auth = auth_check.wrong_create_auth()
        assert invalid_auth.status_code == 200, "Ошибочный статус-код"
        assert invalid_auth.text == '{"reason":"Bad credentials"}', "Ошибка в теле ответа"
        assert invalid_auth.headers["Content-Type"] == ConstHeaders.CONTENT_TYPE_AUTH.value, "Ошибка в headers.Content-Type ответа"
        assert invalid_auth.headers["Content-Length"] == str(len(invalid_auth.text)), "Ошибка: headers.Content-Length != длине тела ответа "
        assert time_ping <= ConstHeaders.MAX_TIME_PING.value, f"Время ответа = {time_ping:.2f} секунд, что превышает лимит ({ConstHeaders.MAX_TIME_PING.value:.2f})"
