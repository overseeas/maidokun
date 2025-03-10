from django.contrib import admin
from .models import RakutenMaidoItem, RakutenMaidoSku, RakutenCoordiroomItem, RakutenCoordiroomSku

admin.site.register(RakutenMaidoItem)
admin.site.register(RakutenMaidoSku)
admin.site.register(RakutenCoordiroomItem)
admin.site.register(RakutenCoordiroomSku)
