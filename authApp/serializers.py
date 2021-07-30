from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *
import gym.utils as ut


class UserCreateSerializer(UserCreateSerializer):

	address = serializers.IntegerField(source='address.id', allow_null=True)

	class Meta(UserCreateSerializer.Meta):
		model = User
		fields = ('id', 'username', 'email', 'first_name', 'last_name', 'address')

	def validate_email(self, value):
		"""
		Check the email format """

		if "@" not in value:
			raise serializers.ValidationError("Email should contain @", code=422)
		if "." not in value:
			raise serializers.ValidationError("Email should contain @", code=422)

	def create(self, validated_data):
		"""
		Strip and capitalize first and last name before user creation """

		strip = lambda x: ut.StripAndCapital(validated_data.get(x))

		validated_data['first_name'] = strip('first_name')
		validated_data['last_name'] = strip('last_name')

		return User.objects.create_user(**validated_data)


class AddressSerializer(serializers.ModelSerializer):

	class Meta:
		model = Address
		fields = ('country', 'city', 'street', 'postcode')

	def validate_postcode(self, value):
		"""
		Check the postcode format """

		if "-" not in value:
			raise serializers.ValidationError("Expected -", code=422)
		postcode = value.split("-")
		if len(postcode) > 2:
			raise serializers.ValidationError("Too many -", code=422)
		if len(postcode[0]) != 2 or len(postcode[1]) != 3:
			raise serializers.ValidationError("Bad postcode format", code=422)
		try:
			int(postcode[0])
			int(postcode[1])
		except Exception as e:
			raise serializers.ValidationError("Poscode should consist of integer values separated with -", code=422)
		return value

	def create(self, validated_data):
		"""
		Strip and capitalize country, city and street before creation """

		strip = lambda x: ut.StripAndCapital(validated_data.get(x))
		validated_data['street'] = strip('street')
		validated_data['country'] = strip('country')
		validated_data['city'] = strip('city')

		return Address.objects.create(**validated_data)