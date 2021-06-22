from django.contrib import admin
from .models import Trainer, TrainerHours, WorkingHours

# Register your models here.

admin.site.register(Trainer)
admin.site.register(TrainerHours)
admin.site.register(WorkingHours)
