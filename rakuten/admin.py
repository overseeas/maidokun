from django.contrib import admin
from .models import Item, Sku, Record #RakutenMaidoItem, RakutenMaidoSku, RakutenCoordiroomItem, RakutenCoordiroomSku

admin.site.register(Item)
admin.site.register(Sku)
admin.site.register(Record)

"""
admin.site.register(RakutenMaidoItem)
admin.site.register(RakutenMaidoSku)
admin.site.register(RakutenCoordiroomItem)
admin.site.register(RakutenCoordiroomSku)
"""