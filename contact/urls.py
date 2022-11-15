from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_contact, name='contacts'),
        path('<contact_id>', views.contact_detail, name='contact_detail'),
]
