from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('currencies.urls')),
    path('users/', include('users.urls')),
    path('subscribe/', include('subscription.urls')),
]
