from django.urls import path
from . import views

urlpatterns = [
	path('activeMemberships/', views.activeMemberships),
	path('renewMembership/<int:id>/', views.renewMembership, name="renewMembership"),
	path('viewProducts/<int:id>/', views.viewProducts, name='viewProducts'),
	path('groupTrainings/', views.viewGroupTrainings, name='viewGroupTrainings'),
	path('signForTraining/<int:id>/', views.signUpForTraining, name='signForTraining'),
	path('viewAllProducts/', views.viewAllProducts, name='viewAllProducts'),
	path('test', views.test, name='test'),
]
