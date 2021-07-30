import json
import coreapi

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import RequestsClient, APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group

import gym.models as GymModels
from authApp.models import Address


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

		# Login created user with credentials
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
		shop = GymModels.Shop.objects.create(
			shop_name='Gym Fit Shop',
			address = self.address
		)
		self.shop_id = shop.id
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
		# Save auth token
		self.token = token_resp.data.get('auth_token')
		# Set generated token as default authentication credentials
		self.requestClient = APIClient()
		self.client.defaults['HTTP_AUTHORIZATION'] = 'Token ' + self.token

	def test_view_address_POST(self):
		""" Testing address creation using API view """

		response = self.client.post(
			'/auth/address/',
			{
				'country': 'PolAnd',
				'city': '   OpoLe',
				'street': 'TeSTIng   ',
				'postcode': '47-224',
			},
			headers={
				'Content-Type':'application/x-www-form-urlencoded'
			}
		)
		self.assertEquals(response.status_code, 200)
		self.assertEquals(response.data.get('country'), 'Poland')
		self.assertEquals(response.data.get('street'), 'Testing')
		self.assertEquals(response.data.get('city'), 'Opole')

	def test_view_address_POST_invalid(self):

		response = self.client.post(
			'/auth/address/',
			{
				'country': 'Poland',
				'city': '   Opole',
				'street': 'Testing',
				'postcode': '47-a24',
			},
		)
		self.assertEquals(response.data.get('postcode')[0], 'Poscode should consist of integer values separated with -')
		self.assertEquals(response.status_code, 422)

	def test_view_membership_GET(self):
		""" Testing membership view using APIClient
			by sending get request to the /membership url """

		#! There is no need to send the headers
		#! just change default HTTP_AUTHORIZATION
		response = self.client.get(
			'http://127.0.0.1:8000/membership/',
			json={}
		)
		self.assertEquals(response.status_code, 200)
		self.assertEquals(len(list(response.data)), 0)
		membership = GymModels.Membership.objects.create(
			membership_type="Open 24",
			membership_price=150
		)
		response = self.client.get(
			'http://127.0.0.1:8000/membership/',
			json={}
		)
		self.assertEquals(response.status_code, 200)
		self.assertEquals(len(list(response.data)), 1)


	""" In progress """
	# def test_view_view_products(self):
	# 	""" Testing viewProducts view using APIClient
	# 	by sending get request to the /product/viewProducts/ url """

	# 	self.client.defaults['Content-Type'] = 'application/x-www-form-urlencoded'

	# 	response1 = self.client.get(
	# 		'http://127.0.0.1:8000/product/viewProducts/',
	# 		data={
	# 			'shopID': 155
	# 		},
	# 		headers={
	# 			'Content-Type':'application/x-www-form-urlencoded'
	# 		}

	# 	)
	# 	print(response1.data)
	# 	self.assertEquals(response1.status_code, 200)



