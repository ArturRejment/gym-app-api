from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import status, serializers
import datetime

import gym.models as GymModels
import gym.serializers as GymSerializers
from authApp.decorators import allowed_users

#!---------------------------------
#!			Group Trainings
#!---------------------------------

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewGroupTrainings(request):
	trainings = GymModels.GroupTraining.objects.all()
	serializer = GymSerializers.GroupTrainingSerializer(trainings, many=True)

	return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['receptionist'])
def createGroupTraining(request):
	serializer = GymSerializers.CreateGroupTrainingSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=200)
	return Response(serializer.errors, status=422)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['member'])
def signUpForTraining(request):
	member = request.user.gymmember
	groupTrainingID = request.data.get('trainingID')

	try:
		groupTraining = GymModels.GroupTraining.objects.get(id=groupTrainingID)
	except Exception:
		raise serializers.ValidationError({'Group Training': [f'There is no group training with id {groupTrainingID}']})

	if groupTraining.signedPeople >= groupTraining.max_people:
		raise serializers.ValidationError({'Error': 'There is already maximum number of people signed for this training'})

	trainSet = groupTraining.grouptrainingschedule_set.all()
	for i, schedule in enumerate(trainSet):
		if trainSet[i].member == member:
			raise serializers.ValidationError({'Error': ['You are alredy signed for this training!']})

	newSchedule = GymModels.GroupTrainingSchedule.objects.create(
		member=member,
		group_training = groupTraining
	)

	return Response('You auspiciously signed for training!')