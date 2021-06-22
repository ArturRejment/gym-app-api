from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import *

class TrainerHoursSerializer(serializers.ModelSerializer):
	working_start = serializers.CharField(source='working.start_time', read_only=True)
	working_finish = serializers.CharField(source='working.finish_time', read_only=True)

	class Meta:
		model = TrainerHours
		fields = ('id', 'working_start', 'working_finish', 'is_active')
