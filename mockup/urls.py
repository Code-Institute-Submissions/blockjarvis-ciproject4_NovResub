from django.urls import path
from . import views

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views


# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('gallery/', views.design_list, name='design_list'),
    path('design/', views.design, name='design'),
    path('', views.create, name='create'),
    path('created_design/', views.created_design, name='created_design'),
    # path('design_form/', views.design_form, name='design_form'),
    # path('designs/new', views.design_create, name='design_create'),
]
