import pytest
from helpers import helper_script


@pytest.fixture
def courier_cleanup():
    created_payloads = []
    yield created_payloads
    for payload in created_payloads:
        try:
            helper_script.delete_courier_by_payload(payload)
        except Exception as e:
            print(f"Не удалось удалить курьера: {payload.get('login')} ({e})")


@pytest.fixture
def order_cleanup():
    created_orders = []
    yield created_orders
    for track in created_orders:
        try:
            helper_script.cancel_order_by_track(track)
        except Exception as e:
            print(f"Не удалось отменить заказ: track={track} ({e})")
