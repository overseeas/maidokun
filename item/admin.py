from django.contrib import admin
from .models import Postage, Supplier, Classification, Maker, Category, Item

# Register your models here.
admin.site.register(Postage)
admin.site.register(Supplier)
admin.site.register(Classification)
admin.site.register(Maker)
admin.site.register(Category)
admin.site.register(Item)
