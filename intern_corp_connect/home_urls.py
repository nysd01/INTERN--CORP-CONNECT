from django.urls import path
from . import home_views

urlpatterns = [
    path('', home_views.home, name='home'),
]