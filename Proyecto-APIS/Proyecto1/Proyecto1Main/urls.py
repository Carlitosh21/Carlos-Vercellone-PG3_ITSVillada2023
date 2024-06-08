from django.urls import path
from .views import api_view

urlpatterns = [
    path('', api_view, name='home'),
    path('Proyecto1Main/views.py', api_view, name='api_view'),
]
