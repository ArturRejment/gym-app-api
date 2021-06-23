from django.db import models
from authApp.models import User

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

	def __str__(self):
		return f'Member {self.user}'

class Receptionist(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	is_senior_receptionist = models.BooleanField(blank=False, null=False, default=False)

	def __str__(self):
		return f'Receptionist {self.user}'

