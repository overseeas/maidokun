from django.contrib import admin
from .models import Item, Stock, Deliverygroup, Category, Maker

# Register your models here.

admin.site.register(Item)
admin.site.register(Stock)
admin.site.register(Deliverygroup)
admin.site.register(Category)
admin.site.register(Maker)