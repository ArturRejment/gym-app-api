from django.db import models
from django.contrib.auth.models import AbstractUser, Group

# Create your models here.

class Address(models.Model):
	country = models.CharField(max_length=250, null = False)
	city = models.CharField(max_length=250, null = False)
	street = models.CharField(max_length=250, null = False)
	postcode = models.CharField(max_length=250, null=False)

	def __str__(self):
		return f'{self.city} {self.street}'


class User(AbstractUser):
	email = models.EmailField(verbose_name='email', max_length=254, unique=True)
	phone = models.CharField(null=True, max_length=250)
	address = models.ForeignKey(Address, verbose_name='address', on_delete=models.CASCADE, null=True, blank=True)

	REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name', 'address']
	USERNAME_FIELD = 'email'

	def __str__(self):
		return f'{self.id} {self.first_name} {self.last_name}'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		group = Group.objects.get(name='member')
		self.groups.add(group)
