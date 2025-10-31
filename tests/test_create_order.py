import requests
import pytest
import allure
from data import urls, data
from helpers import helper_script


@pytest.fixture
def order_cleanup():
    tracks = []
    yield tracks
    for track in tracks:
        helper_script.cancel_order_by_track(track)


class TestCreateOrder:
    @allure.description('Проверка апи создания заказа: /api/v1/orders')
    @allure.feature('Проверка создания заказа')
    @pytest.mark.parametrize('order_data', [
        ("BLACK", 'Проверка создания заказа  с черным самокатом'),
        ("GREY", 'Проверка создания заказа  с серым самокатом'),
        (("BLACK", "GREY"), 'Проверка создания заказа с черным или серым самокатом'),
        ((), 'Проверка создания заказа: Не выбран ни один цвет')
    ])
    def test_create_order(self, order_data, order_cleanup):
        color, title_case = order_data
        payload = data.get_order_data_with_color(color)
        allure.dynamic.title(title_case)

        response = requests.post(urls.create_order_url, json=payload)
        assert response.status_code == 201
        value = response.json()
        assert value['track'] != ''
        order_cleanup.append(value['track'])
