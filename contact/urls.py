from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_contact, name='contacts'),
    path('<int:contact_id>/', views.contact_detail, name='contact_detail'),
    path('add/', views.add_contact, name='add_contact'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
]
