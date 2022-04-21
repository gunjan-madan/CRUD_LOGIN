from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('studentDetails/', views.studentDetails, name='studentDetails'),
    path('register/',views.register, name='register'),
    path('signup/',views.signup, name='signup'),
    path('login/', views.user_login,name='user_login'),
    path('logout/',views.user_logout, name='user_logout')
    
]