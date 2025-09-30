import allure
from src.enums.constant_of_headers import ConstHeaders

class TestPingScenario:

    @allure.title("Проверка ping правильным методом")
    def test_right_ping (self, time_ping, auth_check):
        right_check = auth_check.right_ping()
        assert right_check.status_code == 201, "Ошибочный статус-код"
        assert right_check.text == "Created", "Ошибка в теле ответа"
        assert right_check.headers["Content-Type"] == ConstHeaders.CONTENT_TYPE_PING.value, "Ошибка в headers.Content-Type ответа"
        assert right_check.headers["Content-Length"] == str(len(right_check.text)), "Ошибка: headers.Content-Length != длине тела ответа "
        assert time_ping <= ConstHeaders.MAX_TIME_PING.value, f"Время ответа = {time_ping:.2f} секунд, что превышает лимит ({ConstHeaders.MAX_TIME_PING.value:.2f})"

    @allure.title("Проверка ping неправильным методом")
    def test_bad_ping (self, time_ping, auth_check):
        wrong_check = auth_check.wrong_ping()
        assert wrong_check.status_code == 404, "Ошибочный статус-код"
        assert wrong_check.text == "Not Found", "Ошибка в теле ответа"
        assert wrong_check.headers["Content-Type"] == ConstHeaders.CONTENT_TYPE_PING.value, "Ошибка в headers.Content-Type ответа"
        assert wrong_check.headers["Content-Length"] == str(len(wrong_check.text)), "Ошибка: headers.Content-Length != длине тела ответа "
        assert time_ping <= ConstHeaders.MAX_TIME_PING.value, f"Время ответа = {time_ping:.2f} секунд, что превышает лимит ({ConstHeaders.MAX_TIME_PING.value:.2f})"
