from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('rakuten/<str:pk>', views.rakuten, name="rakuten"),
]