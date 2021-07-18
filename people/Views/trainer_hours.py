from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status

from people.serializers import *
from people.models import GymMember, Trainer
from authApp.decorators import allowed_users, allowed_users_class
import gym.models as GymModels

class TrainerHours(APIView):
	permission_classes = [IsAuthenticated]

	@allowed_users_class(allowed_roles=['trainer'])
	def get(self, request):
		""" View all working hours assigned for specific trainer """
		trainer = request.user.trainer
		trainerHours = trainer.trainerhours_set.all()

		serializer = TrainerHoursSerializer(trainerHours, many=True)
		return Response(serializer.data)

	@allowed_users_class(allowed_roles=['trainer'])
	def put(self, request):
		""" Update specific working hour assigned to trainer """
		trainer = request.user.trainer
		hourID = request.data.get('hourID')
		try:
			updatingHour = trainer.trainerhours_set.get(id = hourID)
		except:
			return Response(data='You have no permissions to update this hour', status=442)

		serializer = TrainerHoursSerializer(instance = updatingHour, data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=422)

	@allowed_users_class(allowed_roles=['trainer'])
	def post(self, request):
		""" Create new trainer's working hour

		@param1 - working
		"""
		trainer = request.user.trainer

		serializer = TrainerWorkingHoursCreateSerializer(
			data={
				'trainer': trainer.id,
				'working': request.data.get('working'),
			}
		)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=201)
		else:
			return Response(serializer.errors, status=422)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['member'])
def viewAvailableTrainers(request):
	""" Get available hours to sing for personal training """

	# Get all trainers
	trainers = Trainer.objects.all()
	# Create a list which contains sets with active hours for every trainer
	acitveHours = [trainer.trainerhours_set.filter(is_active=True).filter(member=None) for trainer in trainers]

	# Prepare a dictionary that will represent serializer
	serializer = {}

	# loop through every set in list (active hours for specific trainer)
	for i, hour in enumerate(acitveHours):
		# Create trainer personal data that will be also a key in serializer
		trainer = str(trainers[i].user).split(" ")
		trainerName = trainer[1] + ' ' + trainer[2]
		# Append all active hours for specific trainer
		serializer[f'{trainerName}'] =  ActiveHoursSerializer(acitveHours[i], many=True).data

	return Response(serializer)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['member'])
def signForPersonalTraining(request):
	""" Sign for personal training

	@param1 - hourID """
	member = request.user.gymmember
	hourID = request.data.get('hourID')
	if hourID == None:
		return serializers.ValidationError({'Missing argument': 'Missing required argument \'hourID\''}, status=422)

	try:
		training = GymModels.TrainerHours.objects.get(id=hourID)
	except Exception:
		return serializers.ValidationError(f'There is no hour with id {hourID}', status=422)

	if training.member != None:
		return serializers.ValidationError(f'There is already someone else signed for this training!', status=422)

	serializer = SignForTrainingSerializer(instance=training, data={'member':member.id})
	if serializer.is_valid():
		serializer.save()
		return Response("Successfully signed for training!", status=200)
	else:
		return serializers.ValidationError(serializer.errors, status=422)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['trainer'])
def viewGroupTrainings(request):
	""" Get all group trainings where trainer is conductor """

	trainer = request.user.trainer

	groupTrainings = trainer.grouptraining_set.all()

	serializer = GroupTrainingsSerializer(groupTrainings, many=True)

	return Response(serializer.data)