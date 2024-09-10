from django.urls import path
from . import views


app_name = "rakuten"

urlpatterns = [
    path('', views.index, name="index"),
    path("update/", views.update, name="update"),
    path('<str:manage_number>/', views.detail, name="detail"),
    
]