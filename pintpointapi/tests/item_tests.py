import json
from rest_framework import status
from rest_framework.test import APITestCase

class ItemTests(APITestCase):
    def setUp(self):
        self.employee = Employee.objects.first()
        token = Token.objects.get(user=self.gamer.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_item(self):
        # Define the endpoint in the API to which
        # the request will be sent
        url = "/items"

        # Define the request body
        data = {
            "type": 1,
            "maker": "beer company",
            "name": "beer",
            "price": 5
        }

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["type"], 1)
        self.assertEqual(json_response["maker"], "beer company")
        self.assertEqual(json_response["name"], "beer")
        self.assertEqual(json_response["price"], 5)