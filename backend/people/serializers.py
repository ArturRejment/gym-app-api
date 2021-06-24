from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import *
from gym.models import *

class TrainerHoursSerializer(serializers.ModelSerializer):
	member = serializers.CharField()
	working_start = serializers.CharField(source='working.start_time', read_only=True)
	working_finish = serializers.CharField(source='working.finish_time', read_only=True)
	# member = serializers.CharField(source='working.member', read_only=False)

	class Meta:
		model = TrainerHours
		fields = ('id', 'working_start', 'working_finish', 'member', 'is_active')

	def update(self, instance, validated_data):
		instance.is_active = validated_data.get('is_active', instance.is_active)
		ident = validated_data.get('member', instance.member)

		if ident != None:
			instance.member = ident
		else:
			instance.member = None

		instance.save()
		return instance

class WorkingHourSerializer(serializers.ModelSerializer):
	class Meta:
		model = WorkingHours
		fields = '__all__'

class ActiveHoursSerializer(serializers.ModelSerializer):
	# user = UserSerializer()
	# workingHours = TrainerHoursSerializer(trainerhours_set.all())
	working = WorkingHourSerializer()
	class Meta:
		model = TrainerHours
		fields = ['id', 'working']