from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import TrainerHoursSerializer, ActiveHoursSerializer, SignForTrainingSerializer
from .models import GymMember, Trainer
from authApp.decorators import allowed_users
import gym.models as gym


@api_view(['GET'])
def index(request):
	member = GymMember.objects.get(id=1)
	context = {
		'Trainer page': member.hasActiveMembership
	}
	return Response(context)

#!------------------------------
#!			Working hours
#!------------------------------

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['trainer'])
def getWorkingHours(request):
	trainer = request.user.trainer
	trainerHours = trainer.trainerhours_set.all()

	serializer = TrainerHoursSerializer(trainerHours, many=True)
	return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['trainer'])
def updateHour(request, **kwargs):
	trainer = request.user.trainer
	try:
		updatingHour = trainer.trainerhours_set.get(id = kwargs['id'])
	except:
		return Response(data='You do not have permissions to update this hour', status=442)

	serializer = TrainerHoursSerializer(instance = updatingHour, data=request.data)

	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		return Response(serializer.errors, status=422)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['member'])
def viewAvailableTrainers(request):
	trainers = Trainer.objects.all()
	acitveHours = [trainer.trainerhours_set.all() for trainer in trainers]
	# activeHour = trainers.trainerhours_set.all()

	serializer = {}

	for i, hour in enumerate(acitveHours):
		trainer = str(trainers[i].user).split(" ")
		trainerName = trainer[1] + ' ' + trainer[2]
		serializer[f'{trainerName}'] =  ActiveHoursSerializer(acitveHours[i], many=True).data

	return Response(serializer)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['member'])
def signForPersonalTraining(request, **kwargs):

	member = request.user.gymmember

	try:
		training = gym.TrainerHours.objects.get(id=kwargs['id'])
	except Exception:
		return Response(f'There is no hour with id {kwargs["id"]}')

	if training.member != None:
		return Response(f'There is already someone else signed for this training!')

	serializer = SignForTrainingSerializer(instance=training, data={'member':member.id})
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		return Response(serializer.errors, status=422)


