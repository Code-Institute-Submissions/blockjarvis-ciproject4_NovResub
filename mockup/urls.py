from django.urls import path
from . import views

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views


# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
	# path('', views.index, name='index'),
    path('', views.mockup, name='mockup'),
    # path('design_form/', views.design_form, name='design_form'),
    # path('designs/new', views.design_create, name='design_create'),
]
