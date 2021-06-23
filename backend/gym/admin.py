from django.contrib import admin
from .models import TrainerHours, WorkingHours, MemberMemberships, Membership

# Register your models here.

admin.site.register(TrainerHours)
admin.site.register(WorkingHours)
admin.site.register(MemberMemberships)
admin.site.register(Membership)