import requests
import allure
from data import urls

@allure.step("Создать курьера")
def api_create_courier(payload):
    return requests.post(urls.create_courier_url, data=payload)

@allure.step("Залогинить курьера")
def api_login_courier(login, password):
    return requests.post(urls.login_courier_url, data={"login": login, "password": password})

@allure.step("Удалить курьера по ID: {courier_id}")
def api_delete_courier_by_id(courier_id):
    if courier_id is None:
        return
    return requests.delete(f"{urls.base_url}/api/v1/courier/{courier_id}", timeout=10)

@allure.step("Создать заказ")
def api_create_order(payload):
    return requests.post(urls.create_order_url, json=payload)

@allure.step("Отменить заказ по треку: {track}")
def api_cancel_order(track):
    return requests.put(urls.cancel_order_url, json={"track": track})

@allure.step("Логин курьера: {payload}")
def api_login_courier_payload(payload):
    return requests.post(urls.login_courier_url, data=payload, timeout=10)

@allure.step("Получить список заказов с параметрами: {params}")
def api_get_orders(params):
    return requests.get(urls.return_order_list_url, params=params, timeout=10)
