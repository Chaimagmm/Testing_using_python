import requests

BASE_URL = "http://localhost:5000"

def test_cart_flow():
    # Add items
    response = requests.post(
        f"{BASE_URL}/add",
        json={"item": "apple", "quantity": 2}
    )
    assert response.status_code == 200

    # Check total
    response = requests.get(f"{BASE_URL}/total")
    assert response.json()["total"] == 2