from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:manage_number>/', views.detail, name="detail"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]