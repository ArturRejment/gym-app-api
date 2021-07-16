from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
import people.models as PeopleModels

def member_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='member')
		instance.groups.add(group)

		# PeopleModels.GymMember.objects.create(
		# 	user=instance
		# )
		# print('Profile created')

post_save.connect(member_profile, sender=User)