from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/',views.register, name='register'),
    path('edit/', views.edit,name='edit'),
    path('deleteEmp/', views.deleteEmp,name='deleteEmp'),

]