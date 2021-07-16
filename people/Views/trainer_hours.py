from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status

from people.serializers import TrainerWorkingHoursCreateSerializer, TrainerHoursSerializer, ActiveHoursSerializer, SignForTrainingSerializer, GroupTrainingsSerializer
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
			return Response(data='You do not have permissions to update this hour', status=442)

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
def signForPersonalTraining(request):

	member = request.user.gymmember
	hourID = request.data.get('hourID')
	if hourID == None:
		return Response({'Missing argument': 'Missing required argument \'hourId\''})

	try:
		training = GymModels.TrainerHours.objects.get(id=hourID)
	except Exception:
		return Response(f'There is no hour with id {hourID}')

	if training.member != None:
		return Response(f'There is already someone else signed for this training!')

	serializer = SignForTrainingSerializer(instance=training, data={'member':member.id})
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		return Response(serializer.errors, status=422)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['trainer'])
def viewGroupTrainings(request):
	trainer = request.user.trainer

	groupTrainings = trainer.grouptraining_set.all()

	serializer = GroupTrainingsSerializer(groupTrainings, many=True)

	return Response(serializer.data)