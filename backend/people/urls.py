from django.urls import path
from . import views
from .Views import workingHours

urlpatterns = [
	path('', views.apiOverview),
	path('workingHours/', workingHours.WorkingHoursView.as_view()),
	path('trainer/working/', views.getWorkingHours),
	path('trainer/updateHour/', views.updateHour),
	path('trainer/viewGroupTrainings/', views.viewGroupTrainings),
	path('viewActiveHours/', views.viewAvailableTrainers),
	path('signForPersonalTraining/', views.signForPersonalTraining),
]
