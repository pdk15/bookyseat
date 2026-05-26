from django.contrib import admin
from django.urls import path
from .views import register , login_view , profile , reset_password  , home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home , name = 'home'),
    path('register/', register , name = 'register'),
    path('login/', login_view , name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout'),
    path('profile/', profile , name = 'profile'),
    path('password-reset/', reset_password , name = 'password_reset'),
    
    path('register/', register , name = 'register'),
]
