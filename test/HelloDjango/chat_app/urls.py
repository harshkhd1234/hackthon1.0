"""
without html template
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
"""
from django.urls import path

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
]