from django.urls import path
from . import home_views

urlpatterns = [
    path('', home_views.home, name='home'),
    path('overview/', home_views.overview, name='overview'),
    path('about/', home_views.about, name='about'),
    path('features/', home_views.features, name='features'),
]