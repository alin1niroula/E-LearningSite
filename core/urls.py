from .views import *
from django.urls import path




urlpatterns = [
    path('', CoreView.as_view(), name='core'),

    ]