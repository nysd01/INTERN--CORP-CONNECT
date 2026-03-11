from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='intern_dashboard'),
    path('search/', views.search_internships, name='search_internships'),
]