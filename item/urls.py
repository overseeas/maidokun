from django.urls import path

from . import views

app_name = "item"
urlpatterns = [
        path("index/", views.index, name="index"),
        path("create/", views.create, name="create"),
        path("detail/<str:item_code>", views.detail, name="detail")
]
