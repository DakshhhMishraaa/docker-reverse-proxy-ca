
import requests

BASE_URL = "http://localhost:8080"


def test_users_service():
    response = requests.get(f"{BASE_URL}/users/")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "User Service"
    assert "users" in data


def test_products_service():
    response = requests.get(f"{BASE_URL}/products/")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "Product Service"
    assert "products" in data


def test_orders_service():
    response = requests.get(f"{BASE_URL}/orders/")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "Order Service"
    assert "orders" in data
