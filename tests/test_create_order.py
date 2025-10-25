import requests
from data import urls
import pytest
import allure
from data import data

class TestCreateOrder:
    @allure.description('Проверка апи создания заказа: /api/v1/orders')
    @allure.feature('Проверка созданя заказа')
    @pytest.mark.parametrize('order_data',[("BLACK", 'Проверка создания заказа  с черным самокатом'),
                                            ("GREY", 'Проверка создания заказа  с серым самокатом'),
                                            (("BLACK", "GREY"), 'Проверка создания заказа с черным или серым самокатом'),
                                            ((), 'Проверка создания заказа: Не выбран ни один цвет')])
    def test_create_courier(self, order_data):
        color, title_case = order_data
        payload = data.get_order_data_with_color(self, color)
        allure.dynamic.title(title_case)
        response = requests.post(urls.create_order_url
            , json=payload
        )
    
        assert response.status_code == 201
        value = response.json()
        assert value['track'] != ''
