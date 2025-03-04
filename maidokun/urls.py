"""
URL configuration for maidokun project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('rakuten/', include('rakuten.urls', namespace="rakuten")),
    path('item/', include('item.urls', namespace="item")),
    path('yahoo/', include('yahoo.urls', namespace="yahoo")),
    path('kakakucom/', include('kakakucom.urls', namespace="kakakucom")),
    path('admin/', admin.site.urls),
    path("", include('home.urls')),
]
