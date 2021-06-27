from rest_framework import serializers
from people.serializers import UserSerializer, TrainerSerializerShort, WorkingHourSerializer
from .models import *
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
		fields = '__all__'

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
		type = validated_data.get('membership_type')

		name = ''
		type = type.split(" ")
		for word in type:
			word = word.capitalize()
			name += word + ' '
		name.strip()

		validated_data['membership_type'] = name

		return Membership.objects.create(**validated_data)
