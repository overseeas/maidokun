from django.contrib import admin
from .models import KakakuStore1Item, KakakuStore2Item, Stock, Deliverygroup, Category, Maker

# Register your models here.

admin.site.register(KakakuStore1Item)
admin.site.register(KakakuStore2Item)
admin.site.register(Stock)
admin.site.register(Deliverygroup)
admin.site.register(Category)
admin.site.register(Maker)