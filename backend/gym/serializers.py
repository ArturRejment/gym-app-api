from rest_framework import serializers
from .models import *
import datetime

class ActiveMembershipsSerializer(serializers.ModelSerializer):

	class Meta:
		model = MemberMemberships
		fields = '__all__'

class RenewMembershipSerializer(serializers.ModelSerializer):

	class Meta:
		model = MemberMemberships
		fields = '__all__'

	def create(self, validated_data):
		validated_data['']
		validated_data['expiry_date'] = datetime.timedelta(days = +30)
		return MemberMemberships.objects.create(**validated_data)