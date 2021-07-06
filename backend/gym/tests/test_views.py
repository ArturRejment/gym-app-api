from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import RequestsClient, APITestCase
from rest_framework.authtoken.models import Token
from gym.models import *
import json

class TestViews(APITestCase):

	# token = Token.objects.get(user__username='lauren')

	def test_shop_view_GET(self):
		# client = Client()

		# client = RequestsClient()
		headers = {
			'Content-Type': 'application/x-www-form-urlencoded'
		}

		response = self.client.post(
			'http://127.0.0.1:8000/auth/users/',
			{
				'username': 'testing',
				'email': 'test@email.com',
				'first_name': 'test_name',
				'last_name': 'test_lname',
				'password': 'StroNGPass2137',
				're-password': 'StroNGPass2137',
				'phone': '123456789',
				'address': '3'
			},
			# headers={
			# 	'Content-Type':'application/x-www-form-urlencoded'
			# },
			# format='json'
		)
		print(response)



