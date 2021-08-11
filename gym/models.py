from django.db import models
from people.models import Trainer, Receptionist, GymMember
from authApp.models import Address


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


class Membership(models.Model):
	membership_type = models.CharField(max_length=200, unique=True)
	membership_price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.membership_type


class MemberMemberships(models.Model):
	membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
	member = models.ForeignKey(GymMember, on_delete=models.CASCADE)
	purchase_date = models.DateField(auto_now_add=True)
	expiry_date = models.DateField()

	def __str__(self):
	 return f'{self.member} has {self.membership} until {self.expiry_date}'


class Product(models.Model):
	product_name = models.CharField(max_length=250)
	product_price = models.DecimalField(max_digits=5, decimal_places=2)
	product_weight = models.IntegerField()

	def __str__(self):
	 return f'{self.product_name} {self.product_weight}g'


class Shop(models.Model):
	shop_name = models.CharField(max_length=250)
	address = models.ForeignKey(Address, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.shop_name} {self.address}'


class ShopProducts(models.Model):
	shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False, blank=False)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
	product_amount = models.IntegerField()

	def __str__(self):
		return f'{self.product} in {self.shop}'


class GroupTraining(models.Model):
	training_name = models.CharField(max_length=250, null=False, blank=False, unique=True)
	trainer = models.ForeignKey(Trainer, null=False, blank=False, on_delete=models.CASCADE)
	time = models.ForeignKey(WorkingHours, null=False, blank=False, on_delete=models.CASCADE)
	max_people = models.IntegerField()
	signed_members = models.ManyToManyField(GymMember, related_name='signed')

	@property
	def signedPeople(self):
		return self.signed_members.count()

	def signInForTraining(self, member):
		""" Sign user in for a training """
		self.signed_members.add(member)

	def signOutFromTraining(self, member):
		""" Sign user out from training """
		self.signed_members.remove(member)

	def isSignedForTraining(self, member):
		""" Returns True if member is alredy signed for training.
		False otherwise """
		self.signed_members.filter(id = member.id).exists()

	def __str__(self):
		return self.training_name

