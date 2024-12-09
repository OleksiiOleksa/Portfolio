from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('solana/', include('solanapage.urls')),  # Этот путь подключает urls приложения solanapage
    path('', include('homepage.urls')),  # Путь для главной страницы
]
