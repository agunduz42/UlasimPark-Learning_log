"""Defines URL patterns for users"""

from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # Login page
    path('login/', views.login_view, name='login_view'),

    # Logout page
    path('logout/', views.logout_view, name='logout_view'),
    
    # registiration page
    path('register/', views.register, name='register'),
]
