from django.contrib import admin

from .models import PurchaseCategory, Purchase

admin.site.register(PurchaseCategory)
admin.site.register(Purchase)

