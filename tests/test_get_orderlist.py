import pytest
import allure
from helpers import api_client


class TestListOrders:
    @allure.description("Проверка апи получения списка заказов: GET /api/v1/orders")
    @allure.feature("Получения списка заказов")
    @pytest.mark.parametrize('headers', [
        {"limit": "1", "page": "0"},
        {"courierId": "641999"},
        {"limit": "10", "nearestStation": '["1","2","3","4"]'},
    ])
    def test_return_order_list(self, headers):
        allure.dynamic.title(f'Получение списка заказа с параметрами {headers}')

        response = api_client.api_get_orders(headers)
        response_body = response.json()

        assert 'orders' in response_body
