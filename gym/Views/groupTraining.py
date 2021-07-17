from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import status, serializers
import datetime

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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['member'])
def signUpForTraining(request):
	"""
	Funtion allows to sign up for a group training

	Required parameters to send with request:
	@param1 - trainingID
	"""
	member = request.user.gymmember
	groupTrainingID = request.data.get('trainingID')

	try:
		groupTraining = GymModels.GroupTraining.objects.get(id=groupTrainingID)
	except Exception:
		raise serializers.ValidationError({'Group Training': [f'There is no group training with id {groupTrainingID}']}, code=422)

	if groupTraining.signedPeople >= groupTraining.max_people:
		raise serializers.ValidationError({'Error': 'There is already maximum number of people signed for this training'}, code=422)

	trainSet = groupTraining.grouptrainingschedule_set.all()
	for i, schedule in enumerate(trainSet):
		if trainSet[i].member == member:
			raise serializers.ValidationError({'Error': ['You are alredy signed for this training!']}, code=422)

	newSchedule = GymModels.GroupTrainingSchedule.objects.create(
		member=member,
		group_training = groupTraining
	)

	return Response('You auspiciously signed for training!')