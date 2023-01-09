import json
from rest_framework import status
from rest_framework.test import APITestCase
from pintpointapi.models import Employee

class TabTests(APITestCase):

    def setUp(self):
        self.employee = Employee.objects.first()
        token = Token.objects.get(user=self.gamer.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_tab(self):
        # Define the endpoint in the API to which
        # the request will be sent
        url = "/tabs"

        # Define the request body
        data = {
            "gameTypeId": 1,
            "skillLevel": 5,
            "title": "Clue",
            "maker": "Milton Bradley",
            "numberOfPlayers": 6,
        }

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["title"], "Clue")
        self.assertEqual(json_response["maker"], "Milton Bradley")
        self.assertEqual(json_response["skill_level"], 5)
    self.assertEqual(json_response["number_of_players"], 6)