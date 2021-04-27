from django.urls import reverse

from rest_framework.test import APITestCase


class BooksApitestCase(APITestCase):
    def test_get(self):
        url = '/api/patients/'
        print(url)
        response = self.client.get(url)
        print(response.data)
