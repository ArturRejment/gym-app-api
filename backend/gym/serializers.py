from rest_framework import serializers
from .models import *

class ActiveMembershipsSerializer(serializers.ModelSerializer):

	class Meta:
		model = MemberMemberships
		fields = '__all__'