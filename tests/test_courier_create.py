import requests
from helpers import helper_script
from data import response_text
from data import urls
import pytest
import allure
from helpers import helper_script



@pytest.fixture
def courier_cleanup():
    created_payloads = []
    yield created_payloads
    for payload in created_payloads:
        helper_script.delete_courier_by_payload(payload)


class TestCreateCourier:
    @allure.description('Проверка апи создания курьера: api/v1/courier')
    @allure.feature('Создание нового курьера')
    @pytest.mark.parametrize('courier_data',[
        (helper_script.generate_new_courier_payload(), 201, response_text.success_response_text, 'Создание нового курьера с корректными данными'),
        (helper_script.register_new_courier_and_return_login_password(), 409, response_text.two_same_courier_response_text, 'Создания курьера с существующим логином'),
        ({"login": "", "password": "qwe321", "firstName": "Тесттестбезлогина"}, 400, response_text.bad_request_response_text, 'Создание курьера при отсутствии обязательные полей: без логина'),
        ({"login": "testoviylogin", "password": "", "firstName": "Тесттестбнзпароля"}, 400, response_text.bad_request_response_text, 'Создание курьера при отсутствии обязательные полей: без ппароля')

    ]) 
    def test_create_courier(self, courier_data, courier_cleanup):
        payload, exp_status_code, exp_text, title_case = courier_data
        allure.dynamic.title(title_case)    
        courier_cleanup.append(payload)
        response = requests.post(urls.create_courier_url, data=payload)
        assert response.status_code == exp_status_code
        assert response.text == exp_text