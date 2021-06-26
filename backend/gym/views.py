from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, serializers
import datetime

from authApp.decorators import allowed_users
import gym.serializers as GymSerializers
import gym.models as GymModels


@api_view(['GET'])
def test(request):
	train = GymModels.GroupTraining.objects.get(id=1)
	context = {
		'Signed in: ': train.signedPeople
	}
	return Response(context)


#!---------------------------------
#!			Memberships
#!---------------------------------

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['receptionist'])
def activeMemberships(request):
	activeMemberships = GymModels.MemberMemberships.objects.filter(expiry_date__gt = datetime.date.today())

	serializer = GymSerializers.ActiveMembershipsSerializer(activeMemberships, many=True)
	return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['member'])
def renewMembership(request):
	member = request.user.gymmember
	membershipID = request.data.get('membershipID')
	if member.hasActiveMembership:
		raise serializers.ValidationError({'Member':'Member already has active membership'})
	try:
		membership = GymModels.Membership.objects.get(id=membershipID)
	except Exception:
		raise serializers.ValidationError({'Membership':f'Membership with id {membershipID} does not exist!'})

	st_date = datetime.date.today()
	end_date = st_date + datetime.timedelta(days=+30)

	newMembership = GymModels.MemberMemberships.objects.create(
		member=member,
		membership=membership,
		expiry_date=end_date
	)

	return Response('Membership created!')


#!---------------------------------
#!			Products
#!---------------------------------

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewProducts(request, **kwargs):
	try:
		shop = GymModels.Shop.objects.get(id = kwargs['id'])
	except Exception:
		return Response(f'There is no shop with id {kwargs["id"]}')

	products = shop.shopproducts_set.all()

	serializer = GymSerializers.ShopProductsSerializer(products, many=True)
	return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['receptionist'])
def viewAllProducts(request):
	products = GymModels.Product.objects.all()
	serializer = GymSerializers.ProductSerializer(products, many=True)
	return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['receptionist'])
def addProduct(request, **kwargs):
	receptionist = request.user.receptionist
	amount = request.data.get('amount')
	if amount == None:
		return Response('Please specify the amount')

	print(receptionist.shop)
	try:
		shop = GymModels.Shop.objects.get(id = receptionist.shop.id)
	except Exception:
		return Response('You have no privileges to manage any shops!')

	try:
		product = GymModels.Product.objects.get(id = kwargs['id'])
	except Exception:
		return Response(f'Product with id {kwargs["id"]} does not exists!')

	shopProducts = shop.shopproducts_set.all()
	for i, prod in enumerate(shopProducts):
		if shopProducts[i].product == product:
			return Response(f'Product {product} already exists in this shop!')

	newProduct = GymModels.ShopProducts.objects.create(
		shop=shop,
		product=product,
		product_amount=amount
	)
	return Response(f'Product {product} added to the shop!')

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
@allowed_users(allowed_roles=['member'])
def signUpForTraining(request, **kwargs):
	member = request.user.gymmember

	try:
		groupTraining = GymModels.GroupTraining.objects.get(id=kwargs['id'])
	except Exception:
		return Response(f'There is no group training with id {kwargs["id"]}')

	if groupTraining.signedPeople >= groupTraining.max_people:
		return Response('There is already maximum number of people signed for this training')

	trainSet = groupTraining.grouptrainingschedule_set.all()
	for i, schedule in enumerate(trainSet):
		if trainSet[i].member == member:
			return Response('You are alredy signed for this training!')

	newSchedule = GymModels.GroupTrainingSchedule.objects.create(
		member=member,
		group_training = groupTraining
	)

	return Response('You auspiciously signed for training!')

