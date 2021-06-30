from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, serializers
from rest_framework.views import APIView
import datetime

from authApp.decorators import allowed_users, allowed_users_class
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['receptionist'])
def createMembership(request):
	serializer = GymSerializers.MembershipSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)

	return Response(serializer.errors, status=422)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewMemberships(request):
	memberships = GymModels.Membership.objects.all()
	serializer = GymSerializers.MembershipSerializer(memberships, many=True)

	return Response(serializer.data, status=200)


#!---------------------------------
#!			Products
#!---------------------------------

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewProducts(request):
	shopID = request.data.get('shopID')
	try:
		shop = GymModels.Shop.objects.get(id = shopID)
	except Exception:
		raise serializers.ValidationError({"ShopID":[f'There is no shop with id {shopID}']})

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
def createProduct(request):
	serializer = GymSerializers.ProductSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	return Response(serializer.errors, status=422)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['receptionist'])
def addProduct(request):
	receptionist = request.user.receptionist
	amount = request.data.get('amount')
	productID = request.data.get('productID')
	if amount == None:
		raise serializers.ValidationError('Please specify the amount')

	print(receptionist.shop)
	try:
		shop = GymModels.Shop.objects.get(id = receptionist.shop.id)
	except Exception:
		raise serializers.ValidationError('You have no privileges to manage any shops!')

	try:
		product = GymModels.Product.objects.get(id = productID)
	except Exception:
		raise serializers.ValidationError(f'Product with id {productID} does not exists!')

	shopProducts = shop.shopproducts_set.all()
	for i, prod in enumerate(shopProducts):
		if shopProducts[i].product == product:
			raise serializers.ValidationError(f'Product {product} already exists in this shop!')

	newProduct = GymModels.ShopProducts.objects.create(
		shop=shop,
		product=product,
		product_amount=amount
	)
	return Response(f'Product {product} added to the shop!')

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['receptionist'])
def deleteProductFromTheShop(request):
	receptionist = request.user.receptionist
	shopProductId = request.data.get('shopProduct')
	shopProduct = GymModels.ShopProducts.objects.get(id=shopProductId)
	shop = shopProduct.shop
	if shop != receptionist.shop:
		raise serializers.ValidationError({'Error': 'This product is not in your shop!'})
	shopProduct.delete()
	return Response('Product deleted')

#!---------------------------------
#!			   Shop
#!---------------------------------

class ShopView(APIView):
	permission_classes = [IsAuthenticated]

	@allowed_users_class(allowed_roles=['receptionist'])
	def get(self, request):
		shops = GymModels.Shop.objects.all()
		serializer = GymSerializers.ShopSerializer(shops, many = True)
		return Response(serializer.data)

	def post(self, request):
		address = request.data.get('address')

		name = request.data.get('shop_name')

		serializer = GymSerializers.ShopSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=200)
		return Response(serializer.errors, status=422)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewShops(request):
	shops = GymModels.Shop.objects.all()
	serializer = GymSerializers.ShopSerializer(shops, many=True)

	return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['receptionist'])
def createShop(request):

	address = request.data.get('address')

	name = request.data.get('shop_name')

	serializer = GymSerializers.ShopSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=200)
	return Response(serializer.errors, status=422)

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

