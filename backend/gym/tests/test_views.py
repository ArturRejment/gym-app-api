from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import RequestsClient, APITestCase, APIClient
from rest_framework.authtoken.models import Token
from gym.models import *
import json

# class TestViews(APITestCase):


# 	def test_shop_view_GET(self):
# 		# client = Client()
# 		token = Token.objects.get(user=14)
# 		print(token)

# 		client = APIClient()

# 		response = self.client.get(
# 			'/auth/token/login',
# 			{
# 				'email': 'baga@gmail.com',
# 				'password': '6unguiop'
# 			}
# 			# headers={
# 			# 	'Content-Type':'application/x-www-form-urlencoded'
# 			# },
# 			# format='json'
# 		)
# 		print(response)



