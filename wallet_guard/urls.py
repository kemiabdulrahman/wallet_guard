from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wallet/', include("core.urls", namespace='wallet')),
]
