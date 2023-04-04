from django.urls import path

from .views import *

urlpatterns = [
    path('forms/build', FormsAPI.as_view()),
]
