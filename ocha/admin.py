from django.contrib import admin
from .models import OchaStore1Item, OchaStore2Item, Category, Subcategory

# Register your models here.

admin.site.register(OchaStore1Item)
admin.site.register(OchaStore2Item)
admin.site.register(Category)
admin.site.register(Subcategory)