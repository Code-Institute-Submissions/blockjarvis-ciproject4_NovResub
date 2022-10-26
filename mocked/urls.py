
from django.urls import path
from . import views

from django.contrib.auth import logout


urlpatterns = [
    path('', views.create, name='create'),
]
