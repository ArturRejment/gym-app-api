from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.response import Response


def allowed_users(allowed_roles = []):
    """ Decorator function for function-based views """

    def decorator(view_function):

        def wrapper_func(request, *args, **kwargs):
            groups = None
            # Get all user's roles, if they exists
            if request.user.groups.exists():
                groups = request.user.groups.all()
            # Check if user's role is in allowed roles
            for group in groups:
                # If it is, return desired function (view)
                if group.name in allowed_roles:
                    return view_function(request, *args, **kwargs)
            return Response({"Auth": ["You are not authorized to view the page!"]}, status=403)
            return view_function(request, *args, **kwargs)
        return wrapper_func
    return decorator

def allowed_users_class(allowed_roles = []):
    """ Decorator function for class-based views """

    def decorator(view_function):

        def wrapper_func(self, request, *args, **kwargs):
            group = None
            # Get all user's roles, if they exists
            if request.user.groups.exists():
                groups = request.user.groups.all()
            # Check if user's role is in allowed roles
            for group in groups:
                if group.name in allowed_roles:
                # If it is, return desired function (view)
                    return view_function(self, request, *args, **kwargs)
            return Response({"Auth": ["You are not authorized to view the page!"]}, status=403)
            return view_function(self, request, *args, **kwargs)
        return wrapper_func
    return decorator