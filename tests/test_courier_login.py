import pytest
import allure
from data import data
from helpers import api_client


class TestLoginCourier:
    @allure.description("Проверка апи логина курьера: /api/v1/courier/login")
    @allure.feature("Авторизация")
    @pytest.mark.parametrize("login_data", data.LOGIN_TEST_DATA)
    def test_login_courier(self, login_data):
        payload, exp_status_code, exp_text, title_case = login_data
        allure.dynamic.title(title_case)

        response = api_client.api_login_courier_payload(payload)

        assert response.status_code == exp_status_code
        assert exp_text in response.text
