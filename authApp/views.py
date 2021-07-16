from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView

from .serializers import AddressSerializer
from .decorators import allowed_users_class
from .models import Address


class AddressView(APIView):
	permission_classes = [IsAuthenticated]

	def post(self, request):
		"""
		Create new address
		"""
		serializer = AddressSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=422)

	@allowed_users_class(allowed_roles=['receptionist'])
	def get(self, request):
		"""
		Returns all addresses
		"""
		addresses = Address.objects.all()
		serializer = AddressSerializer(addresses, many=True)
		return Response(serializer.data)