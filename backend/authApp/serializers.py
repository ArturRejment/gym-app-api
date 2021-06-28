from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *

class UserCreateSerializer(UserCreateSerializer):
	address = serializers.IntegerField(source='address.id', allow_null=True)
	class Meta(UserCreateSerializer.Meta):
		model = User
		fields = ('id', 'username', 'email', 'first_name', 'last_name', 'address')

class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = ('country', 'city', 'street', 'postcode')

	def create(self, validated_data):
		return Address.objects.create(**validated_data)