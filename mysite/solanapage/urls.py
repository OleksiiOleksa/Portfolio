# solanapage/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.solana_page, name='solanapage'),
    path('average_price/', views.get_average_price, name='average_price'),
]