# homepage/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('send_feedback/', views.send_feedback, name='send_feedback'),
]
