from django.db import models
from people.models import Trainer, Receptionist, GymMember

# Create your models here.
class TrainerHours(models.Model):
	trainer = models.ForeignKey(Trainer, on_delete=models.DO_NOTHING)
	working = models.ForeignKey('WorkingHours', on_delete=models.DO_NOTHING)
	member = models.ForeignKey(GymMember, on_delete=models.DO_NOTHING, null=True, blank=True)
	is_active = models.BooleanField(blank=True, null=True, default=True)

	def __str__(self):
	 return str(self.trainer) + ' ' + str(self.working)

class WorkingHours(models.Model):
	start_time = models.CharField(max_length=5, null=False, blank=False)
	finish_time = models.CharField(max_length=50, null=False, blank=False)

	def __str__(self):
		return f'{self.start_time} - {self.finish_time}'