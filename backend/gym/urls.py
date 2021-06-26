from django.urls import path
from . import views

urlpatterns = [
	path('activeMemberships/', views.activeMemberships),
	path('renewMembership/', views.renewMembership, name="renewMembership"),
	path('viewProducts/<int:id>/', views.viewProducts, name='viewProducts'),
	path('groupTrainings/', views.viewGroupTrainings, name='viewGroupTrainings'),
	path('signForTraining/<int:id>/', views.signUpForTraining, name='signForTraining'),
	path('viewAllProducts/', views.viewAllProducts, name='viewAllProducts'),
	path('addProduct/<int:id>/', views.addProduct, name='addProduct'),
	path('test', views.test, name='test'),
]
