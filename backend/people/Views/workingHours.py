from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import serializers

import gym.models as GymModels
import gym.serializers as GymSerializers
import people.serializers as PeopleSerializer
from authApp.decorators import allowed_users, allowed_users_class

#!---------------------------
#!		Working hours
#!---------------------------

class WorkingHoursView(APIView):
	permission_classes = [IsAuthenticated]

	@allowed_users_class(allowed_roles=['trainer', 'receptionist'])
	def get(self, request):
		"""
		A function that allows to browse all working hours
		"""
		workingHours = GymModels.WorkingHours.objects.all()
		serializer = PeopleSerializer.WorkingHourSerializer(workingHours, many=True)
		return Response(serializer.data)