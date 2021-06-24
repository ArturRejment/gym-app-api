from django.urls import path
from . import views

urlpatterns = [
	path('activeMemberships/', views.activeMemberships),
	path('renewMembership/<int:id>/', views.renewMembership, name="renewMembership")
]
