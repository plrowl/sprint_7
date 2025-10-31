import requests
import random
import string
from data import urls


def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string


def generate_new_courier_payload():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {"login": login, "password": password, "firstName": first_name}
    return payload


def register_new_courier_and_return_login_password():
    payload = generate_new_courier_payload()
    requests.post(urls.create_courier_url, data=payload)
    return payload


def login_courier_get_id(login, password):
    resp = requests.post(urls.login_courier_url, data={"login": login, "password": password}, timeout=10)
    if resp.status_code != 200:
        return None
    body = resp.json()
    return body.get("id")

def delete_courier_by_id(courier_id):
    if courier_id is None:
        return
    requests.delete(f"{urls.base_url}/api/v1/courier/{courier_id}", timeout=10)

def delete_courier_by_payload(payload):
    login = payload.get("login")
    password = payload.get("password")
    if not login or not password:
        return
    cid = login_courier_get_id(login, password)
    delete_courier_by_id(cid)

def cancel_order_by_track(track):
    requests.put(f"{urls.base_url}/api/v1/orders/cancel", json={"track": track}, timeout=10)