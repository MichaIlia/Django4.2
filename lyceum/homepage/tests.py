from http import HTTPStatus

from django.test import Client, TestCase

from rest_framework import status
from rest_framework.test import APITestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_coffee(self):
        response = Client().get('/coffee/')
        self.assertEqual(response.status_code, 418)



class ExampleTestCase(APITestCase):
    def test_url_root(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code))
