import unittest
from django.test import Client

class SimpleLoginTest(unittest.TestCase):

    def test_home(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_admin(self):
        client = Client()
        response = client.get('/admin')
        self.assertEqual(response.status_code, 200)
    
    def test_login(self):
        client = Client()
        response = client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_api_patients(self):
        client = Client()
        response = client.get('/api/patients')
        self.assertEqual(response.status_code, 200)

    def test_patients(self):
        client = Client()
        response = client.get('/patients')
        self.assertEqual(response.status_code, 200)

    def test_doctors(self):
        client = Client()
        response = client.get('/doctors')
        self.assertEqual(response.status_code, 200)
