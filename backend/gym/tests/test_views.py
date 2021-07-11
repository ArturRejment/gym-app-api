from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import RequestsClient, APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group
import gym.models as GymModels
from authApp.models import Address
import json

class TestAuthenticationViews(APITestCase):
	""" Testing Authentication with API Views """

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


	def test_member_sign_up(self):

		#! Create new user
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

		#! Login created user with credentials
		response = self.client.post(
			'/auth/token/login/',
			{
				'email': 'test@gmail.com',
				'password': 'StronGPassHeRo78423'
			},
			headres={
				'Content-Type':'application/x-www-form-urlencoded'
			}
		)
		# Check if user could login
		self.assertEquals(response.status_code, 200)
		self.assertNotEquals(response.data.get('auth_token'), None)


class TestOpenAccessViews(APITestCase):
	""" Test some open-access views
		Views that can be accessed by anyone who is authenticated """

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


		self.token = token_resp.data.get('auth_token')

	"""! Testing in progress """
	# def test_view_active_hours(self):
	# 	reqClient = APIClient()
	# 	reqClient.credentials(HTTP_AUTHORIZATION='Token '+self.token)
	# 	reqClient.defaults['HTTP_AUTHORIZATION'] = 'Token ' + self.token

	# 	auth_token = f'Token {self.token}'
	# 	auth_headers = {
	# 		# 'Content-Type':'application/json',
	# 		'Accept': '*/*',
	# 		'Connection': 'keep-alive',
	# 		'HTTP_AUTHORIZATION': 'Token ' + self.token
	# 	}
	# 	print(auth_token)
	# 	print(Token.objects.all())
	# 	response = reqClient.get(
	# 		'http://127.0.0.1:8000/shop/',
	# 		json={},
	# 		headers=auth_headers
	# 	)
	# 	print(self.token)
	# 	print(response)
