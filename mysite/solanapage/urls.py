# solanapage/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.solana_page, name='solanapage'),  # Путь к странице Solana
]