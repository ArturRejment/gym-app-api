from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('active/', views.getActiveHours),
	path('updateHour/<int:id>/', views.updateHour)
]
