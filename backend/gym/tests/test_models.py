from django.test import TestCase
import gym.models as GymModels
import gym.serializers as GymSerializers

class TestCapitalNamesModels(TestCase):

	def setUp(self):
		self.membershipData = {
			'membership_type': '  gYm OPEN 24h    WoRKOUT',
			'membership_price': 50,
		}
		self.shopData = {
			'shop_name': '  bEEfy  WEIghts  ',
			'address': 6
		}

	def test_some_models(self):
		""" Test membership creation"""
		serializer = GymSerializers.MembershipSerializer(data=self.membershipData)
		if serializer.is_valid():
			serializer.save()
		self.assertEquals(serializer.data.get('membership_type'), 'Gym Open 24h Workout')