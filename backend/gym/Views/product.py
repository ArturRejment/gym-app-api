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