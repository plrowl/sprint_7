from . import response_text 

ORDER_DATA = {
    "firstName": "Твайлайт",
    "lastName": "Спаркл",
    "address": "Библиотека Золотой Дуб, Понивилль",
    "metroStation": 4,
    "phone": "+7 800 555 35 35",
    "rentTime": 5,
    "deliveryDate": "2025-10-25",
    "comment": "дружба — это чудо",
    "color": []
}

def get_order_data_with_color(color):
    data = dict(ORDER_DATA)
    data['color'] = [color] if color else []
    return data


ORDER_LIST_DATA = {
    "orders": [
        {
            "id": 4,
            "courierId": None,
            "firstName": "Эпплджек",
            "lastName": "Земная пони",
            "address": "ферма  Яблочная аллея",
            "metroStation": "2",
            "phone": "+7 800 555 35 35",
            "rentTime": 4,
            "deliveryDate": "2025-10-25T01:00:00.000Z",
            "track": 400443,
            "color": [
                "BLACK",
                "GREY"
            ],
            "comment": "Йиихааа",
            "createdAt": "2025-10-25T01:00:00.000Z",
            "updatedAt": "2025-10-25T01:00:00.000Z",
            "status": 0
        },
        {
            "id": 5,
            "courierId": None,
            "firstName": "Пинки",
            "lastName": "Пай",
            "address": "Сахарный дворец",
            "metroStation": "4",
            "phone": "+7 800 555 35 35",
            "rentTime": 4,
            "deliveryDate": "2025-10-25T01:00:00.000Z",
            "track": 189237,
            "color": [
                "BLACK",
                "GREY"
            ],
            "comment": "PARTY",
            "createdAt": "2025-10-25T01:00:00.000Z",
            "updatedAt": "2025-10-25T01:00:00.000Z",
            "status": 0
        }
    ],
    "pageInfo": {
        "page": 0,
        "total": 3,
        "limit": 2
    },
    "availableStations": [
        {
            "name": "Черкизовская",
            "number": "2",
            "color": "#D92B2C"
        },
        {
            "name": "Преображенская площадь",
            "number": "3",
            "color": "#D92B2C"
        },
        {
            "name": "Сокольники",
            "number": "4",
            "color": "#D92B2C"
        }
    ]
}


LOGIN_TEST_DATA = [
    ({"login": "pinkie", "password": "party"}, 200, "id", "Проверка логина с корректными данными"),
    (
        {"login": "", "password": "party"},
        400,
        response_text.bad_request_login_response_text,
        "Авторизация с некорректными данными: Отсутствует логин",
    ),
    (
        {"login": "pinkie", "password": ""},
        400,
        response_text.bad_request_login_response_text,
        "Авторизация с некорректными данными: Отсутствует пароль",
    ),
    (
        {"login": "pinkie", "password": "partyparty"},
        404,
        response_text.user_not_found_response_text,
        "Авторизация с некорректными данными: Неправильный пароль",
    ),
    (
        {"login": "pink", "password": "party"},
        404,
        response_text.user_not_found_response_text,
        "Авторизация с некорректными данными: Неправильный логин",
    ),
]
