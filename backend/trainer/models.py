from django.db import models
from authApp.models import User

# Create your models here.

class Trainer(models.Model):
	user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
	number_of_certifications = models.IntegerField(blank=True, null=True)
	years_in_company = models.IntegerField(blank=True, null=True)

	def __str__(self):
	 return f'{self.user.first_name} {self.user.last_name}'

class TrainerHours(models.Model):
	trainer = models.ForeignKey(Trainer, on_delete=models.DO_NOTHING)
	working = models.ForeignKey('WorkingHours', on_delete=models.DO_NOTHING)
	# trainer = models.ForeignKey(Trainer, on_delete=models.DO_NOTHING)
	is_active = models.BooleanField(blank=True, null=True, default=True)

	def __str__(self):
	 return str(self.trainer) + ' ' + str(self.working)

class WorkingHours(models.Model):
	start_time = models.CharField(max_length=5, null=False, blank=False)
	finish_time = models.CharField(max_length=50, null=False, blank=False)

	def __str__(self):
		return f'{self.start_time} - {self.finish_time}'
