import pytest
import allure
from data import data
from helpers import api_client

class TestCreateOrder:
    @allure.description('Проверка апи создания заказа: /api/v1/orders')
    @allure.feature('Проверка создания заказа')
    @pytest.mark.parametrize('order_data', [
        ("BLACK", 'Проверка создания заказа с черным самокатом'),
        ("GREY", 'Проверка создания заказа с серым самокатом'),
        (("BLACK", "GREY"), 'Проверка создания заказа с черным и серым самокатом'),
        ((), 'Проверка создания заказа без выбора цвета')
    ])
    def test_create_order(self, order_data, order_cleanup):
        color, title_case = order_data
        payload = data.get_order_data_with_color(color)
        allure.dynamic.title(title_case)

        response = api_client.api_create_order(payload)
        assert response.status_code == 201

        value = response.json()
        assert value['track'] != ''

        order_cleanup.append(value['track'])
