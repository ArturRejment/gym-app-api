from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status

from .serializers import TrainerHoursSerializer, ActiveHoursSerializer, SignForTrainingSerializer, GroupTrainingsSerializer
from .models import GymMember, Trainer
from authApp.decorators import allowed_users, allowed_users_class
import gym.models as GymModels


@api_view(['GET'])
def apiOverview(request):

	context = {
		'GET': 'GET Method',
		'/auth/users/me/': '[Logged user] returns details about currently logged user',
		'/trainer/working/': '[Trainer] returns details about trainer working hours',
		'/trainer/viewGroupTrainings/' : '[Trainer] returns trainer\'s group trainings',
		'/viewActiveHours/': '[Anyone] returns available training hours',

		'/groupTrainings/': '[Anyone] returns available group trainings',

		'/product/viewProducts/': '[Anyone] returns products currently available in shop specified by id',
		'/product/': '[Receptionist] returns all products that can be added to the shop',

		'/embership/': '[Anyone] allows to browse all membership',
		'/membership/activeMemberships/': '[Receptionist] returns every member who has active membership',

		'/shop/': '[Anyone] allows to view all shops',

		'POST': 'POST Method',
		'/auth/token/login/': '[Anyone] allows to login for the account - returns auth_token if success',
		'/auth/users/ [Anyone]': 'allows to register an Gym Member account',
		'/auth/token/logout/': '[Logged user] allows to logout',
		'/auth/createAddress/': '[Anyone] creates an address',
		'/trainer/updateHour/': '[Trainer] allows to update information about trainer working hour specified by id',
		'/signForPersonalTraining/': '[GymMember] allows to sign for personal training specified by id',

		'/groupTraining/signForTraining/': '[GymMember] allows to sign for group training specified by id',
		'/addProductToShop/': '[Receptionist] allows to add a product to the shop',
		'/product/': '[Receptionist] allows to create a new product',

		'/membership/': '[Receptionist] allows to create a new membership',
		'/membership/renewMembership/': '[GymMember] allows to renew membership',

		'/groupTraining/': '[Receptionist] allows to create a new group training',
		'/shop/': '[Receptionist] allows to create new shop',

		'DELETE': 'DELETE Method',
		'/product/': '[Receptionist] allows to delete particular product form the shop',
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
def updateHour(request):
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


