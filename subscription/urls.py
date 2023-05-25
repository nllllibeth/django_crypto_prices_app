from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.get_subscription_page, name='subscription_page'),
]