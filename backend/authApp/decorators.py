from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.response import Response

def allowed_users(allowed_roles = []):
    def decorator(view_function):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_function(request, *args, **kwargs)
            else:
                return Response({"Auth": ["You are not authorized to view the page!"]}, status=401)

            return view_function(request, *args, **kwargs)


        return wrapper_func
    return decorator