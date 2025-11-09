from helpers import api_client
import random
import string

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
    api_client.api_create_courier(payload)
    return payload

def login_courier_get_id(login, password):
    resp = api_client.api_login_courier(login, password)
    if resp.status_code != 200:
        return None
    return resp.json().get("id")

def delete_courier_by_payload(payload):
    login = payload.get("login")
    password = payload.get("password")
    if not login or not password:
        return
    courier_id = login_courier_get_id(login, password)
    api_client.api_delete_courier_by_id(courier_id)

def cancel_order_by_track(track):
    api_client.api_cancel_order(track)
