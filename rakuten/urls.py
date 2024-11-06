from django.urls import path
from . import views, export, forms


app_name = "rakuten"

urlpatterns = [
    path('', views.index, name="index"),
    path("update/", views.update, name="update"),
    path("export/", export.all_data_for_vlookup, name="export"),
    path('<str:manage_number>/', views.detail, name="detail"),
]