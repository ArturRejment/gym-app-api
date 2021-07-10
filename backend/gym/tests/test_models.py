from django.test import TestCase
import gym.models as GymModels
import authApp.models as AuthModels
import gym.serializers as GymSerializers

class TestCapitalNamesModels(TestCase):

	def setUp(self):
		self.membershipData = {
			'membership_type': '  gYm OPEN 24h    WoRKOUT',
			'membership_price': 50,
		}
		address = AuthModels.Address.objects.create(
			country='Poland',
			city='Honolulu',
			street='Grunwald 15',
			postcode='12-256'
		)
		self.shopData = {
			'shop_name': '  bEEfy  WEIghts  ',
			'address': address.id
		}

	def test_some_models(self):
		""" Test membership creation"""
		membership_serializer = GymSerializers.MembershipSerializer(data=self.membershipData)
		if membership_serializer.is_valid():
			membership_serializer.save()
		self.assertEquals(membership_serializer.data.get('membership_type'), 'Gym Open 24h Workout')

	def test_shop_model(self):
		""" Test shop creation """
		shop_serializer = GymSerializers.ShopSerializer(data=self.shopData)
		if shop_serializer.is_valid():
			shop_serializer.save()
		self.assertEquals(shop_serializer.data.get('shop_name'), 'Beefy Weights')