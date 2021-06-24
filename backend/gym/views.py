from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from authApp.decorators import allowed_users
from .serializers import ActiveMembershipsSerializer
from .models import MemberMemberships, Membership
import datetime

# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['receptionist'])
def activeMemberships(request):
	activeMemberships = MemberMemberships.objects.filter(expiry_date__gt = datetime.date.today())

	serializer = ActiveMembershipsSerializer(activeMemberships, many=True)
	return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@allowed_users(allowed_roles=['member'])
def renewMembership(request, **kwargs):
	member = request.user.gymmember
	if member.hasActiveMembership:
		return Response('Member already has active membership')
	else:
		membership = Membership.objects.get(id = kwargs['id'])
		st_date = datetime.date.today()
		end_date = st_date + datetime.timedelta(days=+30)
		newMembership = MemberMemberships.objects.create(
			member=member,
			membership=membership,
			expiry_date=end_date
		)
		return Response('Membership created!')

