# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Trang chủ
    # Thêm các đường dẫn khác của app core
]