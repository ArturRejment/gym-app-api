from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import RequestsClient, APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group
import gym.models as GymModels
from authApp.models import Address
import json

class TestViews(APITestCase):

	def setUp(self):
		self.address = Address.objects.create(
			country='Poland',
			city='Honolulu',
			street='Ladna 5',
			postcode='15-223',
		)
		Group.objects.create(
			name='member'
		)


	def test_shop_view_GET(self):

		# Create new user
		response = self.client.post(
			'/auth/users/',
			{
				'username': 'test',
				'email': 'test@gmail.com',
				'password': 'StronGPassHeRo78423',
				're_password': 'StronGPassHeRo78423',
				'phone': '123456789',
				'first_name': 'test',
				'last_name': 'testing',
				'address': self.address,
			},
			headers={
				'Content-Type':'application/x-www-form-urlencoded'
			},
		)
		# Check if user was created
		self.assertEquals(response.status_code, 201)



