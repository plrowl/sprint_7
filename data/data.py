def get_order_data_with_color(self, color):
    order_request = {
    "firstName": "Твайлайт",
    "lastName": "Спаркл",
    "address": "Библиотека Золотой Дуб, Понивилль",
    "metroStation": 4,
    "phone": "+7 800 555 35 35",
    "rentTime": 5,
    "deliveryDate": "2025-10-25",
    "comment": "дружба — это чудо",
    "color": [color] if color else []}
    return order_request


def get_order_list(self):
    order_list_request = {
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
    return order_list_request