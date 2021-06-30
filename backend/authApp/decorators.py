from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.response import Response

def allowed_users(allowed_roles = []):
    def decorator(view_function):
        def wrapper_func(request, *args, **kwargs):

            groups = None

            if request.user.groups.exists():
                groups = request.user.groups.all()

            for group in groups:
                if group.name in allowed_roles:
                    return view_function(request, *args, **kwargs)

            return Response({"Auth": ["You are not authorized to view the page!"]}, status=401)

            return view_function(request, *args, **kwargs)

        return wrapper_func
    return decorator

def allowed_users_class(allowed_roles = []):
    def decorator(view_function):
        def wrapper_func(self, request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                groups = request.user.groups.all()


            for group in groups:
                print(group.name)
                if group.name in allowed_roles:
                    return view_function(self, request, *args, **kwargs)

            return Response({"Auth": ["You are not authorized to view the page!"]}, status=401)

            return view_function(self, request, *args, **kwargs)


        return wrapper_func
    return decorator