import requests
from data import response_text
from data import urls
import pytest
import allure


class TestLoginCourier:
    @allure.description("Проверка апи логина курьера: /api/v1/courier/login")
    @allure.feature("АВторизация")
    @pytest.mark.parametrize(
        "login_data",
        [
            ({"login": "pinkie", "password": "party"}, 200, "id", "Проверка логина с корректными данными"),
            (
                {"login": "", "password": "party"},
                400,
                response_text.bad_request_login_response_text, "АВторизация с некорректными данными: Отсутствует логин"
            ),
            (
                {"login": "pinkie", "password": ""},
                400,
                response_text.bad_request_login_response_text, "АВторизация  с некорректными данными: Отсутствует пароль"
            ),
            (
                {"login": "pinkie", "password": "partyparty"},
                404,
                response_text.user_not_found_response_text, "АВторизация  с некорректными данными: Неправильный пароль"
            ),
            (
                {"login": "pink", "password": "party"},
                404,
                response_text.user_not_found_response_text, "АВторизация  с некорректными данными: Неправильный логин"
            ),
        ], 
    )
    def test_create_courier(self, login_data):
        payload, exp_status_code, exp_text, title_case = login_data
        allure.dynamic.title(title_case)

        response = requests.post(urls.login_courier_url, data=payload)
        assert response.status_code == exp_status_code
        assert exp_text in response.text
