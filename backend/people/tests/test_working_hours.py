from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import Group

import gym.models as GymModels
from authApp.models import Address, User

class TestWorkingHours(APITestCase):
	""" Testing Working Hours Views """

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
		trainer_group = Group.objects.create(
			name='trainer'
		)
		self.client.post(
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

		client = User.objects.get(username = 'test')
		client.groups.add(trainer_group)

		token_resp = self.client.post(
			'/auth/token/login/',
			{
				'email': 'test@gmail.com',
				'password': 'StronGPassHeRo78423'
			},
			headers={
				'Content-Type':'application/x-www-form-urlencoded'
			}
		)


		# Save auth token
		self.token = token_resp.data.get('auth_token')
		# Set generated token as default authentication credentials
		self.client.defaults['HTTP_AUTHORIZATION'] = 'Token ' + self.token

		GymModels.WorkingHours.objects.create(
			start_time='12:30',
			finish_time='13:30'
		)

	def test_working_hours_view_POST(self):
		""" Test workingHours/ API endpoint POST method """
		response = self.client.post(
			'/workingHours/',
			{
				'start_time': '13:30',
				'finish_time': '14:30'
			},
			headers={
				'Content-Type':'application/x-www-form-urlencoded'
			}
		)

		self.assertEquals(response.status_code, 200)

	def test_working_hours_view_GET(self):
		""" Test workingHours/ API endpoint GET method """
		response = self.client.get(
			'/workingHours/',
			headers={
				'Content-Type':'application/x-www-form-urlencoded'
			}
		)

		print(response)

		self.assertEquals(response.status_code, 200)


