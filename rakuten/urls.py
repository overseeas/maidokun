from django.urls import path
from . import views, export, forms


app_name = "rakuten"

urlpatterns = [
    path('index/', views.index, name="index"),
    path("update/", views.update, name="update"),
    path("export/", export.all_data_for_vlookup, name="export"),
    path('detail/<str:manage_number>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path("", views.index, name="index"),
]
