from django.test import SimpleTestCase
from django.urls import reverse, resolve
import gym.Views.membership as memb
import gym.Views.product as prod

class TestMembershipUrls(SimpleTestCase):

	def test_membership(self):
		url = reverse('viewMembership')
		self.assertEquals(resolve(url).func.view_class, memb.MembershipView)

	def test_active_membership(self):
		url = reverse('activeMembership')
		self.assertEquals(resolve(url).func, memb.activeMemberships)

	def test_renewMembership(self):
		url = reverse('renewMembership')
		self.assertEquals(resolve(url).func, memb.renewMembership)

class TestProductUrls(SimpleTestCase):

	def test_product(self):
		url = reverse('productView')
		self.assertEquals(resolve(url).func.view_class, prod.ProductView)

	def test_view_product(self):
		url = reverse('viewProducts')
		self.assertEquals(resolve(url).func, prod.viewProducts)

	def test_add_product(self):
		url = reverse('addProduct')
		self.assertEquals(resolve(url).func, prod.addProduct)