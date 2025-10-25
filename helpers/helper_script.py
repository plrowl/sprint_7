import requests
import random
import string
from data import urls

def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string

def register_new_courier_and_return_login_password():
    # создаём список, чтобы метод мог его вернуть
    login_pass = [] 

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {"login": login, "password": password, "firstName": first_name}

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(urls.create_courier_url, data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return payload


def generate_new_courier_payload():
    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {"login": login, "password": password, "firstName": first_name}

    # возвращаем список
    return  payload