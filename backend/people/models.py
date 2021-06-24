from django.db import models
from authApp.models import User
import gym
import datetime

# Create your models here.

class Trainer(models.Model):
	user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
	number_of_certifications = models.IntegerField(blank=True, null=True)
	years_in_company = models.IntegerField(blank=True, null=True)

	def __str__(self):
	 return f'Trainer {self.user}'

class GymMember(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	sign_up_date = models.DateField(auto_now_add=True)
	is_suspended = models.BooleanField(blank=False, default=False)
	account_credit = models.FloatField(null=False)

	@property
	def hasActiveMembership(self):
		try:
			membership = gym.models.MemberMemberships.objects.filter(member=self.id, expiry_date__gt=datetime.date.today())
			print(membership)
		except Exception:
			membership = None

		if membership != None and membership.count() != 0:
			return True
		else:
			return False

	def __str__(self):
		return f'Member {self.user}'

class Receptionist(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	is_senior_receptionist = models.BooleanField(blank=False, null=False, default=False)
	shop = models.ForeignKey('gym.Shop', on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return f'Receptionist {self.user}'

