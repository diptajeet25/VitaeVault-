from django.contrib import admin
from django.urls import path
from app import views as app_views

urlpatterns = [
    path('', app_views.home, name='home'),
    path('dashboard/', app_views.dashboard, name='dashboard'),
    path('login/', app_views.user_login, name='login'),
    path('signup/', app_views.user_signup, name='signup'),
    path('logout/', app_views.user_logout, name='logout')
]
