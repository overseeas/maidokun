from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('rakuten/', include('rakuten.urls')),
    path('', include('rakuten.urls'))
]
