from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings
from occurrences.models import OccurrenceModel
import requests

User = get_user_model()

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER


class OccurrenceAPITest(APITestCase):
    def setUp(self):
        # Create new user
        new_user = User(username='user-test', email='email@testing.com')
        new_user.set_password('testingpassword')
        new_user.save()

        # Create new occurrence
        new_occurrence = OccurrenceModel.objects.create(
            description="This is a test description",
            latitude=123,
            longitude=123,
            category="ROAD_CONDITION",
            user=new_user
        )

    def test_user_creation(self):
        """
        This test will assert the user created in the setup
        :return:
        """
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_occurrence_creation(self):
        """
        This test will assert the occurrence created in the setup
        :return:
        """
        occurrence_count = OccurrenceModel.objects.count()
        self.assertEqual(occurrence_count, 1)

    def test_get_occurrences_list(self):
        """
        This test will assert the status code from getting the list of occurrences. It must return 200 OK
        :return 200 OK:
        """
        data = {}
        url = reverse("api_occurrences:occurrences")
        # url = 'http://127.0.0.1:8000/api/occurrences/'
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_occurrence(self):
        """
        This test will assert the status code from creating a new occurrence. It must return 200 OK or 401 NOT AUTHORIZED
        :return 401 NOT AUTHORIZED:
        """
        data = {
            "description": "Simple description for test",
            "latitude": 1234.0,
            "longitude": 1234.0,
            "category": "CONSTRUCTION",
        }
        url = reverse("api_occurrences:occurrences")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_occurrences_item(self):
        """
        This test will assert the status code from getting one occurrence. It must return 200 OK
        :return 200 OK:
        """
        occurrence = OccurrenceModel.objects.first()
        data = {}
        url = occurrence.get_absolute_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_occurrence(self):
        """
        This test will assert the status code from creating a new occurrence. It must return 405 OK or 401 NOT AUTHORIZED
        :return 405 METHOD NOT ALLOWED or 401 NOT AUTHORIZED:
        """
        occurrence = OccurrenceModel.objects.first()
        data = {
            "description": "Simple description for test",
            "latitude": 1234.0,
            "longitude": 1234.0,
            "state": "VALIDADO",
            "category": "CONSTRUCTION",
        }
        url = occurrence.get_absolute_url()
        # Try with post, the method is not allowed

        # Try with put, not authorized
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


        '''
    def test_update_occurrence_authorized(self):
        """
        This test will assert the status code from creating a new occurrence. It must return 200 OK
        :return 200 OK:
        """
        occurrence = OccurrenceModel.objects.first()
        data = {
            "description": "Simple description for test",
            "latitude": 1234.0,
            "longitude": 1234.0,
            "state": "RESOLVIDO",
            "category": "CONSTRUCTION",
        }
        #url = occurrence.get_absolute_url()
        url = 'http://127.0.0.1:8000/api/occurrences/1'
        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token_rsp = encode_handler(payload)
        bearer = "Bearer " + token_rsp
        headers = {"Authorization": bearer}
        Http
        response = requests.put(url, data=data, headers=headers).json()
        print(headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)'''