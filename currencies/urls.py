from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_currencies, name='currencies'),
    path('currency/<str:pk>/', views.get_currency, name='currency'),
    path('favourite/<str:pk>/', views.favourite_view, name='favourite_currency'),
    path('favourite_lists/', views.render_favourites, name='favourite_list')
]
