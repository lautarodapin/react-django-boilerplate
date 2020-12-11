from django.urls import path
from django.shortcuts import render

urlpatterns = [
    path('', lambda r, *args, **kwargs: render(r, 'frontend/index.html')),
]
