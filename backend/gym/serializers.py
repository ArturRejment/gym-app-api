from rest_framework import serializers
from people.serializers import UserSerializer
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

class RenewMembershipSerializer(serializers.ModelSerializer):

	class Meta:
		model = MemberMemberships
		fields = '__all__'

	def create(self, validated_data):
		validated_data['']
		validated_data['expiry_date'] = datetime.timedelta(days = +30)
		return MemberMemberships.objects.create(**validated_data)

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