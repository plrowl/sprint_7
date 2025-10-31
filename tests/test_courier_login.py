import requests
from data import urls
from data import data
import pytest
import allure


class TestLoginCourier:
    @allure.description("Проверка апи логина курьера: /api/v1/courier/login")
    @allure.feature("Авторизация")
    @pytest.mark.parametrize("login_data", data.LOGIN_TEST_DATA)
    def test_login_courier(self, login_data):
        payload, exp_status_code, exp_text, title_case = login_data
        allure.dynamic.title(title_case)

        response = requests.post(urls.login_courier_url, data=payload)
        assert response.status_code == exp_status_code
        assert exp_text in response.text