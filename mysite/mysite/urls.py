from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('solana/', include('solanapage.urls')),
    path('tasks/', include('taskmanager.urls')),  
    path('accounts/', include('django.contrib.auth.urls')), 
    path('', include('homepage.urls')),
]
