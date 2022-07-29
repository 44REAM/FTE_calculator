from django.urls import path, include

from . import views, apps

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard')
]