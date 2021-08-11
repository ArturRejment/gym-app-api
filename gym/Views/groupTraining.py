import datetime

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import status, serializers
from rest_framework.exceptions import NotFound

import gym.models as GymModels
import gym.serializers as GymSerializers
from authApp.decorators import allowed_users, allowed_users_class

#!---------------------------------
#!			Group Trainings
#!---------------------------------

class GroupTrainingView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		"""
		Function allows to browse all group trainings
		"""
		trainings = GymModels.GroupTraining.objects.all()
		serializer = GymSerializers.GroupTrainingSerializer(trainings, many=True)

		return Response(serializer.data)


	@allowed_users_class(allowed_roles=['receptionist', 'trainer'])
	def post(self, request):
		"""
		Function allows to create new group training

		Required parameters to send with request:
		@param1 - training_name
		@param2 - trainer
		@param3 - time
		@param4 - max_people
		"""
		serializer = GymSerializers.CreateGroupTrainingSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=200)
		return Response(serializer.errors, status=422)

	@allowed_users_class(allowed_roles=['receptionist'])
	def delete(self, request):
		"""
		Function to delete group training

		Required parameters to send with request:
		@param1 - trainingID
		"""
		trainingID = request.data.get('trainingID')
		try:
			training = GymModels.GroupTraining.objects.get(id = trainingID)
		except Exception as e:
			raise serializers.ValidationError({"trainingID": e}, code=422)
		else:
			training.delete()
			return Response("Training deleted successfully")


class SignForGroupTraining(APIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = GymSerializers.GroupTrainingSerializer

	@allowed_users_class(allowed_roles=['member'])
	def post(self, request, **kwargs):
		""" POST method to sign in for group training

		Args:
			**kwargs: send GroupTraining id
		"""
		group_training_id = kwargs['id']
		try:
			group_training = GymModels.GroupTraining.objects.get(id=group_training_id)
		except GymModels.GroupTraining.DoesNotExist:
			raise NotFound('Group training with this id does not exist')

		member = request.user.gymmember
		group_training.signInForGroupTraining(member)
		serializer = self.serializer_class(group_training)
		return Response(serializer.data, status=200)


	@allowed_users_class(allowed_roles=['member'])
	def delete(self, request, **kwargs):
		""" DELETE method to sign in for group training

		Args:
			**kwargs: send GroupTraining id
		"""
		group_training_id = kwargs['id']
		try:
			group_training = GymModels.GroupTraining.objects.get(id=group_training_id)
		except GymModels.GroupTraining.DoesNotExist:
			raise NotFound('Group training with this id does not exist')

		member = request.user.gymmember
		group_training.signOutFromGroupTraining(member)
		serializer = self.serializer_class(group_training)
		return Response(serializer.data, status=200)


