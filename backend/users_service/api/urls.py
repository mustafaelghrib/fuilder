"""
This module defines the urls of the users views.

Variables:
    - urlpatterns: A list of url patterns of users views.
"""

from django.urls import path

from .views import *

urlpatterns = [
    path('users/register', UserRegisterAPI.as_view()),
    path('users/login', UserLoginAPI.as_view()),
]
