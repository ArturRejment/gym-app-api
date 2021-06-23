from django.contrib import admin
from .models import TrainerHours, WorkingHours

# Register your models here.

admin.site.register(TrainerHours)
admin.site.register(WorkingHours)