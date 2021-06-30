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