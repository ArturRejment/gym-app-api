from rest_framework import serializers
from people.serializers import UserSerializer, TrainerSerializerShort, WorkingHourSerializer
from authApp.serializers import AddressSerializer
import people.serializers as PeopleSerializers
from .models import *
import gym.utils as ut
import datetime

class MemberSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = GymMember
		fields='__all__'

class ActiveMembershipsSerializer(serializers.ModelSerializer):
	member = serializers.CharField()
	membership_data = serializers.CharField(source='membership')

	class Meta:
		model = MemberMemberships
		fields = ('id', 'member', 'membership_data', 'purchase_date', 'expiry_date')

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['id', 'product_name', 'product_price', 'product_weight']

	def validate_product_price(self, value):
		"""
		Check if product_price is not negative
		"""
		if value <= 0:
			raise serializers.ValidationError('Price cannot be negative!')
		return value

	def validate_product_weight(self, value):
		"""
		Check if product_weight is not neative
		"""
		if value <= 0:
			raise serializers.ValidationError('Weight cannot be negative!')
		return value

	def create(self, validated_data):
		"""
		Strip and capitalize name before creating object
		"""
		name = validated_data.get('product_name')
		name = ut.StripAndCapital(name)
		validated_data['product_name'] = name

		return Product.objects.create(**validated_data)


class ShopProductsSerializer(serializers.ModelSerializer):
	product = ProductSerializer()
	price = serializers.DecimalField(source='product.product_price',max_digits=5, decimal_places=2)
	class Meta:
		model = ShopProducts
		fields = ('product', 'product_amount', 'price')

class GroupTrainingSerializer(serializers.ModelSerializer):
	trainer = TrainerSerializerShort()
	time = WorkingHourSerializer()
	class Meta:
		model = GroupTraining
		fields = ('id', 'training_name', 'trainer', 'time')


class CreateGroupTrainingSerializer(serializers.ModelSerializer):
	# time = serializers.IntegerField()
	# trainer = TrainerSerializerShort()
	# time = WorkingHourSerializer()
	class Meta:
		model = GroupTraining
		fields = ('id', 'training_name', 'trainer', 'time', 'max_people')

	def create(self, validated_data):

		name = validated_data.get('training_name')
		name = ut.StripAndCapital(name)
		validated_data['training_name'] = name
		return GroupTraining.objects.create(**validated_data)


class SignForGroupTrainingSerializer(serializers.ModelSerializer):
	member = MemberSerializer()
	groupTrainingID = serializers.IntegerField()

	class Meta:
		model = GroupTrainingSchedule
		fields = ('id', 'member', 'groupTrainingID')

	def validate_groupTrainingID(self, value):
		try:
			groupTraining = GroupTraining.objects.get(id = value)
		except Exception:
			raise serializers.ValidationError('Invalid group training id!')

	def save(self, validated_data):
		return GroupTrainingSchedule.objects.create(**validated_data)

class MembershipSerializer(serializers.ModelSerializer):
	class Meta:
		model = Membership
		fields = ['id', 'membership_type', 'membership_price']

	def create(self, validated_data):
		"""
		Strip and capitalize membership_type before cration
		"""
		type = validated_data.get('membership_type')
		name = ut.StripAndCapital(type)
		validated_data['membership_type'] = name

		return Membership.objects.create(**validated_data)

class ShopSerializer(serializers.ModelSerializer):
	# address = AddressSerializer()
	class Meta:
		model = Shop
		fields = ['id', 'shop_name', 'address']

	def create(self, validated_data):
		"""
		Strip and capitalize shop_name before creation
		"""
		name = validated_data.get('shop_name')
		name = ut.StripAndCapital(name)
		validated_data['shop_name'] = name

		return Shop.objects.create(
			**validated_data
		)