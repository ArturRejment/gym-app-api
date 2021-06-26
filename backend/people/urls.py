from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview),
	path('trainer/working/', views.getWorkingHours),
	path('trainer/updateHour/<int:id>/', views.updateHour),
	path('viewActiveHours/', views.viewAvailableTrainers),
	path('signForPersonalTraining/<int:id>/', views.signForPersonalTraining),
]
