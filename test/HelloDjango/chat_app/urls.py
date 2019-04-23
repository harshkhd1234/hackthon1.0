"""
without html template
from django.urls import path

from . import views
python manage.py createsuperuserpython manage.py createsuperuser
urlpatterns = [
    path('', views.index, namepython manage.py createsuperuser='index'),
]
"""
from django.urls import path

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
]
from .views import HomePageView1

urlpatterns = [
    path('', HomePageView1.as_view(), name='h'),
]
