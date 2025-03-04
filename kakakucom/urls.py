from django.urls import path

from . import views

app_name = "kakakucom"
urlpatterns = [
        path("index/", views.index, name="index"),
        path("create/", views.create, name="create"),
        path("detail/<str:code>", views.detail, name="detail")
]
