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
#!			Memberships
#!---------------------------------

class MembershipView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		"""
		Function that allows to view all memberships
		"""
		memberships = GymModels.Membership.objects.all()
		serializer = GymSerializers.MembershipSerializer(memberships, many=True)

		return Response(serializer.data, status=200)

	@allowed_users_class(allowed_roles=['receptionist'])
	def post(self, request):
		"""
		A function that allows to create new membership

		Required parameters to send with request:
		@param1 - membership_type
		@param2 - membership_price
		"""
		serializer = GymSerializers.MembershipSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors, status=422)

	@allowed_users_class(allowed_roles=['receptionist'])
	def delete(self, request):
		"""
		A function to delete membership

		Required parameters to send with request:
		@param1 - membershipID
		"""
		membershipID = request.data.get('membershipID')
		try:
			membership = GymModels.Membership.objects.get(id = membershipID)
		except Exception as e:
			raise serializers.ValidationError(e, code=422)
		else:
			membership.delete()
			return Response("Membership deleted successfully")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['receptionist'])
def activeMemberships(request):
	"""
	A function that allows to browse all active memberships
	"""
	activeMemberships = GymModels.MemberMemberships.objects.filter(expiry_date__gt = datetime.date.today())

	serializer = GymSerializers.ActiveMembershipsSerializer(activeMemberships, many=True)
	return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['member'])
def renewMembership(request):
	"""
	A function that allows to renew a membership

	Required parameters to send with request:
	@param1 - membershipID
	"""
	member = request.user.gymmember
	membershipID = request.data.get('membershipID')
	if member.hasActiveMembership:
		raise serializers.ValidationError({'Member':'Member already has active membership'}, code=422)
	try:
		membership = GymModels.Membership.objects.get(id=membershipID)
	except Exception:
		raise serializers.ValidationError({'Membership':f'Membership with id {membershipID} does not exist!'}, code=422)

	st_date = datetime.date.today()
	end_date = st_date + datetime.timedelta(days=+30)

	newMembership = GymModels.MemberMemberships.objects.create(
		member=member,
		membership=membership,
		expiry_date=end_date
	)

	return Response('Membership created!')



