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

	@allowed_users_class(allowed_roles=['trainer', 'receptionist'])
	def post(self, request):
		"""
		A function that allows to create new working hour

		Required parameters to send with request:
		@param1 - start_time
		@param2 - finish_time
		"""
		serializer = PeopleSerializer.WorkingHourSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=200)
		return Response(serializer.errors, status=422)