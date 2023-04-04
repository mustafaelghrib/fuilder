from django.urls import path

from .views import *

urlpatterns = [
    path('forms', FormListAPI.as_view()),
    path('forms/<form_id>', FormDetailAPI.as_view()),
]
