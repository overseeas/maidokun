from django.urls import path
from . import views, export, forms


app_name = "rakuten"

urlpatterns = [
    path('search/', views.search, name="search"),
    path("update/", views.update, name="update"),
    path("export/", export.all_data_for_vlookup, name="export"),
    path('detail/<str:manage_number>/', views.detail, name="detail"),
    path("", views.search, name="search"),
]
