from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import AddressSerializer

@api_view(['POST'])
def createAddress(request):
	serializer = AddressSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		return Response(serializer.errors, status=422)