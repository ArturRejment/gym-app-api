from django.urls import path
from . import views
from .Views import workingHours
import people.Views.trainer_hours as trainer_hours

urlpatterns = [
	path('', views.apiOverview),
	path('workingHours/', workingHours.WorkingHoursView.as_view()),
	path('trainer/', trainer_hours.TrainerHours.as_view()),
	path('trainer/viewGroupTrainings/', trainer_hours.viewGroupTrainings),
	path('viewActiveHours/', trainer_hours.viewAvailableTrainers),
	path('signForPersonalTraining/', trainer_hours.signForPersonalTraining),
]
