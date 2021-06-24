from django.contrib import admin
from .models import TrainerHours, WorkingHours, MemberMemberships, Membership, Shop, Product, ShopProducts

# Register your models here.

admin.site.register(TrainerHours)
admin.site.register(WorkingHours)
admin.site.register(MemberMemberships)
admin.site.register(Membership)
admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(ShopProducts)