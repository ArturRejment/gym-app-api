from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import serializers

import gym.models as GymModels
import gym.serializers as GymSerializers
from authApp.decorators import allowed_users, allowed_users_class

#!---------------------------------
#!			   Shop
#!---------------------------------

class ShopView(APIView):
	permission_classes = [IsAuthenticated]

	@allowed_users_class(allowed_roles=['receptionist'])
	def get(self, request):
		"""
		A Function that allows to view all shops
		"""
		shops = GymModels.Shop.objects.all()
		serializer = GymSerializers.ShopSerializer(shops, many = True)
		return Response(serializer.data)

	@allowed_users_class(allowed_roles=['receptionist'])
	def post(self, request):
		"""
		A function that allows to add a new shop

		Required parameters to send with request:
		@param1 - address
		@param2 - shop_name
		"""
		address = request.data.get('address')

		name = request.data.get('shop_name')

		serializer = GymSerializers.ShopSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=200)
		return Response(serializer.errors, status=422)

	@allowed_users_class(allowed_roles=['receptionist'])
	def delete(self, request):
		"""
		A function that allows to delete shop managed by receptionist
		"""
		receptionist = request.user.receptionist
		print(receptionist.shop)
		if receptionist.shop == None:
			raise serializers.ValidationError("There is no shop owned by this receptionist!")

		shop = GymModels.Shop.objects.get(id=receptionist.shop.id)
		receptionist.shop = None
		shop.delete()
		return Response("Shop deleted successfully")
