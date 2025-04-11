from locust import HttpUser, task

class CartUser(HttpUser):
    @task
    def test_cart(self):
        self.client.post("/add", json={"item": "book", "quantity": 1})