from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('employee/', views.employee, name = 'employee'),
    path('employer/', views.employer, name = 'employer'),
    path('login/', views.login, name = 'login'),
    path('registration/', views.registration, name = 'registration'),
]