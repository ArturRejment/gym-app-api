from django.contrib import admin
from .models import Trainer, GymMember, Receptionist

# Register your models here.

admin.site.register(Trainer)
admin.site.register(GymMember)
admin.site.register(Receptionist)
