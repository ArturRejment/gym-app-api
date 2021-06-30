from django.urls import path
from . import views
import gym.Views.shop as ShopViews
import gym.Views.product as ProductView
import gym.Views.membership as MembershipView
import gym.Views.groupTraining as GroupTrainingView

urlpatterns = [
	#! Memberships
	path('membership/', MembershipView.MembershipView.as_view(), name="viewMemberships"),
	path('membership/activeMemberships/', MembershipView.activeMemberships),
	path('membership/renewMembership/', MembershipView.renewMembership, name="renewMembership"),

	#! Products
	path('product/', ProductView.ProductView.as_view(), name='productView'),
	path('product/viewProducts/', ProductView.viewProducts, name='viewProducts'),
	path('product/addProductToShop/', ProductView.addProduct, name='addProduct'),
	path('product/deleteProduct/', ProductView.deleteProductFromTheShop, name='deleteProduct'),

	#! Group trainings
	path('groupTraining/', GroupTrainingView.GroupTrainingView.as_view(), name='viewGroupTrainings'),
	path('groupTraining/signForTraining/', GroupTrainingView.signUpForTraining, name='signForTraining'),

	#! Shop
	path('shop/', ShopViews.ShopView.as_view(), name="shop"),
]
