import datetime

from django.test import TestCase
from django.contrib.auth.models import Group

import gym.models as GymModels
import authApp.models as AuthModels
import people.models as PeopleModels
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


class TestProperties(TestCase):
	""" Testing some popular and often used models properties """

	def setUp(self):
		""" Prepare new objects for testing """

		Group.objects.create(
			name='member'
		)
		address = AuthModels.Address.objects.create(
			country='Poland',
			city='Honolulu',
			street='Grunwald 15',
			postcode='12-256'
		)
		self.user1 = AuthModels.User.objects.create(
			username='test1',
			email='test1@gmail.com',
			phone='23232323',
			first_name='Testing',
			last_name='Tester',
			address=address
		)
		self.user2 = AuthModels.User.objects.create(
			username='test2',
			email='test2@gmail.com',
			phone='23232323',
			first_name='Testing',
			last_name='Tester',
			address=address
		)
		self.user3 = AuthModels.User.objects.create(
			username='test3',
			email='test3@gmail.com',
			phone='23232323',
			first_name='Testing',
			last_name='Tester',
			address=address
		)
		self.membership = GymModels.Membership.objects.create(
			membership_type='Open',
			membership_price=100
		)

		self.trainer = PeopleModels.Trainer.objects.create(
			user=self.user1,
			number_of_certifications=5,
			years_in_company=2
		)

		self.workingHour = GymModels.WorkingHours.objects.create(
			start_time='11:15',
			finish_time='12:15'
		)

		self.group_training = GymModels.GroupTraining.objects.create(
			training_name='Full Body Workout',
			trainer=self.trainer,
			time=self.workingHour,
			max_people = 3
		)
		self.member1 = PeopleModels.GymMember.objects.create(
			user=self.user2,
			account_credit=200
		)
		self.member2 = PeopleModels.GymMember.objects.create(
			user=self.user3,
			account_credit=600
		)

	def test_hasActiveMembership_property(self):
		""" Testing hasActiveMembership property """

		# At the beginning no one should have active membership
		self.assertFalse(self.member1.hasActiveMembership)
		self.assertFalse(self.member2.hasActiveMembership)

		# Renew membership for member1
		st_date = datetime.date.today()
		end_date = st_date + datetime.timedelta(days=+30)
		newMemberMembership = GymModels.MemberMemberships.objects.create(
			membership=self.membership,
			member=self.member1,
			expiry_date=end_date
		)

		# Only member1 should have active membership
		self.assertTrue(self.member1.hasActiveMembership)
		self.assertFalse(self.member2.hasActiveMembership)

		# Renew membership for member2
		newMemberMembership = GymModels.MemberMemberships.objects.create(
			membership=self.membership,
			member=self.member2,
			expiry_date=end_date
		)

		# Both member1 and mamber2 should have active memberships
		self.assertTrue(self.member1.hasActiveMembership)
		self.assertTrue(self.member2.hasActiveMembership)

	def test_signedPeople_property(self):
		""" Testing signedPeople property """

		# No people signed for training
		self.assertEquals(self.group_training.signedPeople, 0)

		# One person signed for the training
		self.assertEquals(self.group_training.signedPeople, 1)

		# Two people signed for the training
		self.assertEquals(self.group_training.signedPeople, 2)


		# One person left signed for the training
		self.assertEquals(self.group_training.signedPeople, 1)

