from django.urls import path
from . import views, export


app_name = "rakuten"

urlpatterns = [
    path('', views.index, name="index"),
    path("update/", views.update, name="update"),
    path("export/", export.all_data_for_vlookup, name="export"),
    path("testexport", export.item_and_sku, name="testexport"),
    path('<str:manage_number>/', views.detail, name="detail"),
]