from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview),
	path('trainer/working/', views.getWorkingHours),
	path('trainer/updateHour/', views.updateHour),
	path('trainer/viewGroupTrainings/', views.viewGroupTrainings),
	path('viewActiveHours/', views.viewAvailableTrainers),
	path('signForPersonalTraining/', views.signForPersonalTraining),
]
