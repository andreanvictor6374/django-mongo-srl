from django.contrib import admin

from apps.market.models import Product, Order

admin.site.register(Product)
admin.site.register(Order)