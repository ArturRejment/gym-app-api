from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import *
import gym.models as GymModels

class UserSerializerShort(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'phone')

class TrainerSerializerShort(serializers.ModelSerializer):
	user = UserSerializerShort()
	class Meta:
		model = Trainer
		fields = ('id', 'user')

class TrainerHoursSerializer(serializers.ModelSerializer):
	member = serializers.CharField()
	working_start = serializers.CharField(source='working.start_time', read_only=True)
	working_finish = serializers.CharField(source='working.finish_time', read_only=True)
	# member = serializers.CharField(source='working.member', read_only=False)

	class Meta:
		model = GymModels.TrainerHours
		fields = ('id', 'working_start', 'working_finish', 'member', 'is_active')

	def validate_member(self, value):
		try:
			member = GymMember.objects.get(id=value)
		except:
			raise serializers.ValidationError("Wrong member id given!")
		return value

	def update(self, instance, validated_data):
		instance.is_active = validated_data.get('is_active', instance.is_active)
		ident = validated_data.get('member', instance.member)

		if ident != None:
			instance.member = GymMember.objects.get(id= ident)
		else:
			instance.member = None

		instance.save()
		return instance

class SignForTrainingSerializer(serializers.ModelSerializer):
	class Meta:
		model = GymModels.TrainerHours
		fields = ['member']

	def validate_hourID(self, value):
		try:
			hour = GymModels.TrainerHours.objects.get(id = value)
		except Exception:
			raise serializers.ValidationError("Wrong hourID given!")

	def update(self, instance, validated_data):
		ident = validated_data.get('member', instance.member)

		instance.member = ident

		instance.save()
		return instance

class WorkingHourSerializer(serializers.ModelSerializer):
	class Meta:
		model = GymModels.WorkingHours
		fields = ('id', 'start_time', 'finish_time')

	def validate_start_time(self, value):
		"""
		Check if the start_time has proper format
		"""
		if ":" not in value:
			raise serializers.ValidationError("Bad format! Expected ':'")

		splitted = value.split(":")
		if (len(splitted) > 2):
			raise serializers.ValidationError("Bad format! Too many :")

		hour = splitted[0]
		minute = splitted[1]
		if (len(hour) > 2 or len(minute) > 2):
			raise serializers.ValidationError("Bad format! Too many digits of hours or minutes")

		try:
			hour = int(hour)
			minute = int(minute)
		except Exception as e:
			raise serializers.ValidationError(e)

		if hour < 0 or hour > 24:
			raise serializers.ValidationError("Bad format! The hour value is out of range")
		if minute < 0 or minute > 59:
			raise serializers.ValidationError("Bad format! The minute value is out of range")

		return value

	def validate_finish_time(self, value):
		"""
		Check if finish_time has proper format
		"""
		if ":" not in value:
			raise serializers.ValidationError("Bad format! Expected ':'")

		splitted = value.split(":")
		if (len(splitted) > 2):
			raise serializers.ValidationError("Bad format! Too many :")

		hour = splitted[0]
		minute = splitted[1]
		if (len(hour) > 2 or len(minute) > 2):
			raise serializers.ValidationError("Bad format! Too many digits of hours or minutes")

		try:
			hour = int(hour)
			minute = int(minute)
		except Exception as e:
			raise serializers.ValidationError(e)

		if hour < 0 or hour > 24:
			raise serializers.ValidationError("Bad format! The hour value is out of range")
		if minute < 0 or minute > 59:
			raise serializers.ValidationError("Bad format! The minute value is out of range")

		return value


	def validate(self, data):
		"""
		Check if the start is before finish
		"""
		super().validate(data)
		start = data.get('start_time')
		finish = data.get('finish_time')

		start = start.split(":")
		finish = finish.split(":")

		if int(start[0]) > int(finish[0]):
			raise serializers.ValidationError("Finish must occur after start")
		if int(start[0]) == int(finish[0]):
			if int(start[1]) > int(finish[1]):
				raise serializers.ValidationError("Finish must occur after start")

		return data




class ActiveHoursSerializer(serializers.ModelSerializer):
	# user = UserSerializer()
	# workingHours = TrainerHoursSerializer(trainerhours_set.all())
	working = WorkingHourSerializer()
	class Meta:
		model = GymModels.TrainerHours
		fields = ['id', 'working']

class GroupTrainingsSerializer(serializers.ModelSerializer):
	time = WorkingHourSerializer()
	class Meta:
		model = GymModels.GroupTraining
		fields = ('training_name', 'id', 'time', 'max_people', 'signedPeople')
