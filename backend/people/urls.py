from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('trainer/active/', views.getActiveHours),
	path('trainer/updateHour/<int:id>/', views.updateHour)
]
